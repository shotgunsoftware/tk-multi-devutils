# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'yes_no_dialog.ui'
#
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from tank.platform.qt import QtCore, QtGui

class Ui_YesNoDialog(object):
    def setupUi(self, YesNoDialog):
        YesNoDialog.setObjectName("YesNoDialog")
        YesNoDialog.resize(361, 40)
        YesNoDialog.setModal(True)
        self.horizontalLayout = QtGui.QHBoxLayout(YesNoDialog)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(YesNoDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.yes = QtGui.QPushButton(YesNoDialog)
        self.yes.setObjectName("yes")
        self.horizontalLayout.addWidget(self.yes)
        self.no = QtGui.QPushButton(YesNoDialog)
        self.no.setObjectName("no")
        self.horizontalLayout.addWidget(self.no)
        self.always = QtGui.QPushButton(YesNoDialog)
        self.always.setObjectName("always")
        self.horizontalLayout.addWidget(self.always)

        self.retranslateUi(YesNoDialog)
        QtCore.QMetaObject.connectSlotsByName(YesNoDialog)

    def retranslateUi(self, YesNoDialog):
        YesNoDialog.setWindowTitle(QtGui.QApplication.translate("YesNoDialog", "Shotgun Publish", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("YesNoDialog", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.yes.setText(QtGui.QApplication.translate("YesNoDialog", "Yes", None, QtGui.QApplication.UnicodeUTF8))
        self.no.setText(QtGui.QApplication.translate("YesNoDialog", "No", None, QtGui.QApplication.UnicodeUTF8))
        self.always.setText(QtGui.QApplication.translate("YesNoDialog", "Always", None, QtGui.QApplication.UnicodeUTF8))

from . import resources_rc
