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

logger = sgtk.platform.get_logger(__name__)


class QtLogHandler(logging.Handler):
    """
    Log handler which emits to a given text edit widget.
    """

    def __init__(self, text_edit_widget):
        """
        :param text_edit_widget: QPlainTextEdit widget to emit logs to
        """
        super(QtLogHandler, self).__init__()
        self._text_edit_widget = text_edit_widget

    def emit(self, record):
        """
        Emit the given log record
        :param record: Std log record.
        """
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
