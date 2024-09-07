# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from tank.platform.qt import QtCore
for name, cls in QtCore.__dict__.items():
    if isinstance(cls, type): globals()[name] = cls

from tank.platform.qt import QtGui
for name, cls in QtGui.__dict__.items():
    if isinstance(cls, type): globals()[name] = cls


from  . import resources_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(513, 301)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stackedWidget = QStackedWidget(Dialog)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_input = QWidget()
        self.page_input.setObjectName(u"page_input")
        self.gridLayout = QGridLayout(self.page_input)
        self.gridLayout.setObjectName(u"gridLayout")
        self.copy_config = QCheckBox(self.page_input)
        self.copy_config.setObjectName(u"copy_config")
        self.copy_config.setChecked(True)

        self.gridLayout.addWidget(self.copy_config, 4, 1, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_6, 1, 0, 1, 2)

        self.label_3 = QLabel(self.page_input)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.path = QLineEdit(self.page_input)
        self.path.setObjectName(u"path")

        self.gridLayout.addWidget(self.path, 3, 1, 1, 1)

        self.label_5 = QLabel(self.page_input)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setWordWrap(True)

        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 2)

        self.browse = QToolButton(self.page_input)
        self.browse.setObjectName(u"browse")

        self.gridLayout.addWidget(self.browse, 3, 2, 1, 1)

        self.label_4 = QLabel(self.page_input)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(17, 37, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 5, 0, 1, 2)

        self.config_name = QLineEdit(self.page_input)
        self.config_name.setObjectName(u"config_name")

        self.gridLayout.addWidget(self.config_name, 2, 1, 1, 1)

        self.stackedWidget.addWidget(self.page_input)
        self.page_success = QWidget()
        self.page_success.setObjectName(u"page_success")
        self.gridLayout_2 = QGridLayout(self.page_success)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalSpacer_2 = QSpacerItem(20, 31, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 0, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(90, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 1, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.page_success)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(64, 64))
        self.label.setMaximumSize(QSize(64, 64))
        self.label.setPixmap(QPixmap(u":/tk_multi_devutils_create_sb/complete.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label)

        self.label_7 = QLabel(self.page_success)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setWordWrap(True)

        self.horizontalLayout_2.addWidget(self.label_7)

        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(90, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 31, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_3, 2, 1, 1, 1)

        self.stackedWidget.addWidget(self.page_success)

        self.verticalLayout.addWidget(self.stackedWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.action_button = QPushButton(Dialog)
        self.action_button.setObjectName(u"action_button")

        self.horizontalLayout.addWidget(self.action_button)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)

        self.stackedWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Create Config Sandbox", None))
#if QT_CONFIG(tooltip)
        self.copy_config.setToolTip(QCoreApplication.translate("Dialog", u"If you tick this, the configuration will be copied into the location automatically.\n"
"If you leave it blank, you have to manually add a configuration, for example via source control.\n"
"If you select a folder which already contains files, copying will be disabled.", None))
#endif // QT_CONFIG(tooltip)
        self.copy_config.setText(QCoreApplication.translate("Dialog", u"Copy configuration into folder", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Config Name", None))
#if QT_CONFIG(tooltip)
        self.path.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Create a configuration sandbox on disk where you can make configuration changes, retrieve updates and do development.", None))
        self.browse.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Location on disk", None))
        self.label.setText("")
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Configuration Successfully created. Reload to pick up your changes.", None))
        self.action_button.setText(QCoreApplication.translate("Dialog", u"Proceed", None))
    # retranslateUi
