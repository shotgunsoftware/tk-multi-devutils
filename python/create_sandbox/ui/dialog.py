# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from tank.platform.qt import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(513, 316)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget = QtGui.QStackedWidget(Dialog)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_input = QtGui.QWidget()
        self.page_input.setObjectName("page_input")
        self.gridLayout = QtGui.QGridLayout(self.page_input)
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtGui.QLabel(self.page_input)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 2)
        spacerItem = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 2)
        self.browse = QtGui.QToolButton(self.page_input)
        self.browse.setObjectName("browse")
        self.gridLayout.addWidget(self.browse, 3, 2, 1, 1)
        self.label_3 = QtGui.QLabel(self.page_input)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.page_input)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(17, 37, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 4, 0, 1, 2)
        self.path = QtGui.QLineEdit(self.page_input)
        self.path.setObjectName("path")
        self.gridLayout.addWidget(self.path, 3, 1, 1, 1)
        self.config_name = QtGui.QLineEdit(self.page_input)
        self.config_name.setObjectName("config_name")
        self.gridLayout.addWidget(self.config_name, 2, 1, 1, 1)
        self.stackedWidget.addWidget(self.page_input)
        self.page_success = QtGui.QWidget()
        self.page_success.setObjectName("page_success")
        self.gridLayout_2 = QtGui.QGridLayout(self.page_success)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem2 = QtGui.QSpacerItem(20, 31, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 0, 1, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(90, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtGui.QLabel(self.page_success)
        self.label.setMinimumSize(QtCore.QSize(64, 64))
        self.label.setMaximumSize(QtCore.QSize(64, 64))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/tk_multi_devutils_create_sb/complete.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.label_7 = QtGui.QLabel(self.page_success)
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 1, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(90, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 1, 2, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(20, 31, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem5, 2, 1, 1, 1)
        self.stackedWidget.addWidget(self.page_success)
        self.verticalLayout.addWidget(self.stackedWidget)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.action_button = QtGui.QPushButton(Dialog)
        self.action_button.setObjectName("action_button")
        self.horizontalLayout.addWidget(self.action_button)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Create Config Sandbox", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog", "Create a configuration sandbox on disk where you can make configuration changes, retrieve updates and do development.", None, QtGui.QApplication.UnicodeUTF8))
        self.browse.setText(QtGui.QApplication.translate("Dialog", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "Config Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "Location on disk", None, QtGui.QApplication.UnicodeUTF8))
        self.path.setToolTip(QtGui.QApplication.translate("Dialog", "If you specify an empty folder, you will be prompted if you would like the configuration to be automatically copied into place.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Dialog", "Configuration Successfully created. Reload to pick up your changes.", None, QtGui.QApplication.UnicodeUTF8))
        self.action_button.setText(QtGui.QApplication.translate("Dialog", "Proceed", None, QtGui.QApplication.UnicodeUTF8))

from . import resources_rc
