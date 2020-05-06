# Copyright (c) 2018 Shotgun Software Inc.
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

from sgtk.platform.qt import QtCore, QtGui
from .ui.dialog import Ui_Dialog
from .loghandler import QtLogHandler
from .interact import QtInteraction

logger = sgtk.platform.get_logger(__name__)


class AppDialog(QtGui.QWidget):
    """
    Pops up a dialog and executes tank updates.
    """

    def __init__(self, command_name, parent=None):
        """
        :param str command_name: Name of tank command to execute.
        :param parent: The parent QWidget for this control
        """
        QtGui.QWidget.__init__(self, parent)

        self._bundle = sgtk.platform.current_bundle()

        self._command_name = command_name
        self._command_obj = None

        # set up the UI
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # set up log redirection to UI for tank commands.
        self._logger = logging.getLogger("tank_command")
        self._logger.setLevel(logging.INFO)
        self._handler = QtLogHandler(self.ui.log)
        self._handler.setLevel(logging.INFO)
        self._logger.addHandler(self._handler)

        # set up interaction interface
        self._interaction_interface = QtInteraction(self)

        self.ui.cancel.clicked.connect(self._cancel)

        # automatically start update after a short delay
        QtCore.QTimer.singleShot(400, self._doit)

    def _doit(self):
        """
        Execute the tank updates command
        """

        self._command_obj = self._bundle.sgtk.get_command(self._command_name)
        self._command_obj.set_logger(self._logger)
        self._command_obj.execute({}, self._interaction_interface)
        self._command_obj = None

        self._logger.info("")
        self._logger.info(
            "The command has finished execution. Press Close to continue."
        )

        # turn cancel button into close button
        self.ui.cancel.setEnabled(True)
        self.ui.cancel.setText("Close")
        self.ui.cancel.clicked.connect(self.close)

        reload = self._interaction_interface.ask_yn_question(
            "Would you like to restart the engine to reload your changes?"
        )
        if reload:
            sgtk.platform.restart()

    def _cancel(self):
        """
        Cancel execution
        """
        if self._command_obj:
            self._command_obj.terminate()

        # wait for tank command to complete
        self.ui.cancel.setText("Terminating...")
        self.ui.cancel.setEnabled(False)
