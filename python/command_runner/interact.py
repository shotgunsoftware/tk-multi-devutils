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
from sgtk.platform.qt import QtCore, QtGui

logger = sgtk.platform.get_logger(__name__)


class QtInteraction(sgtk.CommandInteraction):
    def __init__(self, parent):
        self._parent = parent
        self._always_enabled = False

    @property
    def supports_interaction(self):
        """
        True if interaction is supported, false if not.
        """
        return True

    def request_input(self, message):
        """
        Request general input from the user.

        :param str message: Message to display
        :returns: Information entered by user.
        :rtype: str
        """
        input, ok = QtGui.QInputDialog.getText(self._parent, "ShotGrid", message)
        return input

    def ask_yn_question(self, message):
        """
        Prompts the user with a yes/no question.

        :param str message: Message to display
        :returns: True if user selects yes, false if no.
        """
        logger.warning("Yn")
        res = QtGui.QMessageBox.question(
            self._parent,
            "ShotGrid",
            message,
            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No,
        )

        if res == QtGui.QMessageBox.Yes:
            return True
        else:
            return False

    def ask_yna_question(self, message, force_prompt=False):
        """
        Prompts the user with a yes/no/always question.

        Always means that further calls to this method will return True.

        :param str message: Message to display
        :param bool force_prompt: Force a prompt, even if always
            has been selected in the past.
        :returns: True if user selects yes, false if no.
        """
        logger.warning("Yna")
        if self._always_enabled and not force_prompt:
            # always clicked
            return True

        res = QtGui.QMessageBox.question(
            self._parent,
            "ShotGrid",
            message,
            QtGui.QMessageBox.Yes | QtGui.QMessageBox.YesToAll | QtGui.QMessageBox.No,
        )

        if res == QtGui.QMessageBox.YesToAll:
            self._always_enabled = True
            return True
        elif res == QtGui.QMessageBox.Yes:
            return True
        else:
            return False
