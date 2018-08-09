# Copyright (c) 2017 Shotgun Software Inc.
#
# CONFIDENTIAL AND PROPRIETARY
#
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights
# not expressly granted therein are reserved by Shotgun Software Inc.

import sgtk
import logging

from contextlib import nested
from sgtk.platform.qt import QtCore, QtGui
from .ui.dialog import Ui_Dialog
from .redirect import StderrRedirector, StdinRedirector, StdoutRedirector

from .yes_no_dialog import YesNoDialog

# import frameworks
settings = sgtk.platform.import_framework("tk-framework-shotgunutils", "settings")
help_screen = sgtk.platform.import_framework("tk-framework-qtwidgets", "help_screen")
task_manager = sgtk.platform.import_framework("tk-framework-shotgunutils", "task_manager")
shotgun_model = sgtk.platform.import_framework("tk-framework-shotgunutils", "shotgun_model")
shotgun_globals = sgtk.platform.import_framework("tk-framework-shotgunutils", "shotgun_globals")

logger = sgtk.platform.get_logger(__name__)

class QtLogHandler(logging.Handler):

    def __init__(self, text_edit_widget):
        super(QtLogHandler, self).__init__()
        self._text_edit_widget = text_edit_widget

    def emit(self, record):
        log_entry = self.format(record)
        text = self._text_edit_widget.toPlainText()
        text += log_entry
        text += "\n"
        self._text_edit_widget.setPlainText(text)

        # scroll to bottom
        self._text_edit_widget.verticalScrollBar().setValue(
            self._text_edit_widget.verticalScrollBar().maximum()
        )
        QtCore.QCoreApplication.processEvents()


class AppDialog(QtGui.QWidget):
    """
    Main dialog window for the App
    """

    def __init__(self, parent=None):
        """
        :param parent: The parent QWidget for this control
        """
        QtGui.QWidget.__init__(self, parent)

        self._bundle = sgtk.platform.current_bundle()

        # set up the UI
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # these are used to redirect stdout/stderr to the signals
        self._stdout_redirect = StdoutRedirector()
        self._stderr_redirect = StderrRedirector()
        self._stdin_redirect = StdinRedirector(self._readline)

        self._stdout_redirect.output.connect(self._on_stdout)
        self._stderr_redirect.error.connect(self._on_stderr)

        self._logger = logging.getLogger("tank_command")
        self._logger.setLevel(logging.INFO)
        self._handler = QtLogHandler(self.ui.plainTextEdit)
        self._handler.setLevel(logging.INFO)
        self._logger.addHandler(self._handler)

        self._previous_stdout_stderr_line = ""

        self.ui.cancel.clicked.connect(self.close)

        # automatically start update after a short delay
        QtCore.QTimer.singleShot(400, self._doit)

    # todo - proper deinit on close

    def _doit(self):

        with nested(self._stdout_redirect, self._stdin_redirect):
            updates_cmd = self._bundle.sgtk.get_command("updates")
            updates_cmd.set_logger(self._logger)
            updates_cmd.execute({"supress_prompts": False})

        self.ui.cancel.setText("Close")

    def _on_stdout(self, content):

        text = self.ui.plainTextEdit.toPlainText()
        text += content
        text += "\n"
        self.ui.plainTextEdit.setPlainText(text)
        self._previous_stdout_stderr_line = content
        # scroll to bottom
        self._text_edit_widget.verticalScrollBar().setValue(
            self._text_edit_widget.verticalScrollBar().maximum()
        )
        QtCore.QCoreApplication.processEvents()

    def _on_stderr(self, content):
        text = self.ui.plainTextEdit.toPlainText()
        text += content
        text += "\n"
        self.ui.plainTextEdit.setPlainText(text)
        self._previous_stdout_stderr_line = content
        # scroll to bottom
        self._text_edit_widget.verticalScrollBar().setValue(
            self._text_edit_widget.verticalScrollBar().maximum()
        )

        QtCore.QCoreApplication.processEvents()

    def _readline(self):
        """
        Reads a line of input text from the user.

        :return: a string for the user input.
        """
        if "[Yna?]" in self._previous_stdout_stderr_line:
            # this is a std toolkit Yes, no always prompt
            dialog = YesNoDialog(
                self._previous_stdout_stderr_line,
                show_always=True,
                parent=self
            )
            dialog.exec_()
            return dialog.value + "\n"

        elif "[yn]" in self._previous_stdout_stderr_line:
            # this is a std toolkit [yn] prompt
            dialog = YesNoDialog(
                self._previous_stdout_stderr_line,
                show_always=False,
                parent=self
            )
            dialog.exec_()
            return dialog.value + "\n"

        else:
            # general input catch-all
            dialog = QtGui.QInputDialog(
                parent=self,
                flags=QtCore.Qt.FramelessWindowHint
            )
            dialog.setLabelText(self._previous_stdout_stderr_line)
            dialog.adjustSize()

            dialog.resize(self.width(), dialog.height())
            dialog.move(
                self.mapToGlobal(self.rect().topLeft()).x(),
                self.mapToGlobal(self.rect().bottomLeft()).y() - dialog.height()
            )

            try:
                if dialog.exec_() == QtGui.QDialog.Accepted:
                    return str(dialog.textValue()) + "\n"
                else:
                    return ""
            finally:
                self.setFocus()

