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
from .ui.yes_no_dialog import Ui_YesNoDialog

logger = sgtk.platform.get_logger(__name__)


class YesNoDialog(QtGui.QDialog):
    """
    Yes No Dialog overlay to be used in conjuntion with the main updates window.

    Intended to be called as a modal dialog. It will pop up as a frameless
    window overlay at the bottom of the parent window. After the user has
    made a selection, the ``value`` property can be used to retrieve the
    selected value.
    """

    def __init__(self, label, show_always=False, parent=None):
        """
        :param label: Label for the UI
        :param show_always: Should the always button be shown?
        :param parent: The parent QWidget for this control
        """
        QtGui.QDialog.__init__(self, parent)

        self.setWindowFlags(self.windowFlags() | QtCore.Qt.FramelessWindowHint)

        # set up the UI
        self.ui = Ui_YesNoDialog()
        self.ui.setupUi(self)

        self.ui.label.setText(label)
        self.ui.always.setVisible(show_always)

        # position at the bottom of the parent UI
        self.move(
            parent.mapToGlobal(parent.rect().topLeft()).x()+2,
            parent.mapToGlobal(parent.rect().bottomLeft()).y() - self.height() - 4
        )
        self.resize(parent.width()-4, self.height())

        self._value = "N"
        self.ui.yes.clicked.connect(self._on_yes)
        self.ui.no.clicked.connect(self._on_no)
        self.ui.always.clicked.connect(self._on_always)

    @property
    def value(self):
        """
        The selected outcome as a string,
        either 'Y', 'N' or 'A'
        """
        return self._value

    def _on_yes(self):
        self._value = "Y"
        self.close()

    def _on_no(self):
        self._value = "N"
        self.close()

    def _on_always(self):
        self._value = "A"
        self.close()
