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
import urllib
import os
from sgtk.platform.qt import QtCore, QtGui

from .ui.dialog import Ui_Dialog

# import frameworks
settings = sgtk.platform.import_framework("tk-framework-shotgunutils", "settings")
help_screen = sgtk.platform.import_framework("tk-framework-qtwidgets", "help_screen")
overlay = sgtk.platform.import_framework("tk-framework-qtwidgets", "overlay_widget")
task_manager = sgtk.platform.import_framework("tk-framework-shotgunutils", "task_manager")
shotgun_model = sgtk.platform.import_framework("tk-framework-shotgunutils", "shotgun_model")
shotgun_globals = sgtk.platform.import_framework("tk-framework-shotgunutils", "shotgun_globals")

logger = sgtk.platform.get_logger(__name__)


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

        # spinner widget
        # now inside your app constructor, create an overlay and parent it to something
        self._overlay = overlay.ShotgunOverlayWidget(self.ui.page_input)

        # populate a default name for the sandbox
        default_name = "Config Sandbox"
        user_data = sgtk.util.get_current_user(self._bundle.sgtk)
        if user_data and "name" in user_data:
            default_name = "%s's Config Sandbox" % user_data["name"]
        self.ui.config_name.setText(default_name)

        self.ui.browse.clicked.connect(self._browse)
        self.ui.action_button.clicked.connect(self._process)

    def _browse(self):
        """
        shows a file browser
        """

        dialog = QtGui.QFileDialog()
        dialog.setOption(QtGui.QFileDialog.ShowDirsOnly)
        dialog.setFileMode(QtGui.QFileDialog.Directory)
        result = dialog.exec_()
        if result == QtGui.QDialog.Accepted:
            files = dialog.selectedFiles()
            if len(files) > 0:
                self.ui.path.setText(files[0])

    def _process(self):
        """
        Create a new configuration
        """
        path = self.ui.path.text()
        if isinstance(path, unicode):
            path = path.decode("utf-8")

        # validate the name
        if self.ui.config_name.text() == "":
            QtGui.QMessageBox.critical(
                self,
                "No config name specified!",
                "Please specify a name for your configuration."
            )
            return

        # validate the path
        if path == "":
            QtGui.QMessageBox.critical(
                self,
                "No path specified!",
                "Please specify a path to your config sandbox."
            )
            return

        # if directory is empty, ask if we should copy stuff
        if not os.path.exists(path):
            QtGui.QMessageBox.critical(
                self,
                "Path does not exist!",
                "The path '%s' does not exist." % path
            )
            return

        copy_files = False
        files = os.listdir(path)
        if len(files) == 0:
            # empty folder - ask if we should copy contents
            answer = QtGui.QMessageBox.question(
                self,
                "Copy configuration?",
                ("The folder you have selected is empty. Would you like "
                "the folder to be prepopulated with the current configuration?"),
                QtGui.QMessageBox.Yes | QtGui.QMessageBox.No | QtGui.QMessageBox.Cancel
            )
            if answer == QtGui.QMessageBox.Cancel:
                return
            elif answer == QtGui.QMessageBox.Yes:
                copy_files = True

        # now you can use the overlay to report things to the user
        try:
            self._overlay.start_spin()
            QtCore.QCoreApplication.processEvents()

            if copy_files:
                config_descriptor = self._bundle.sgtk.configuration_descriptor
                config_descriptor.copy(path)
                sgtk.util.filesystem.safe_delete_folder(
                    os.path.join(path, "tk-metadata")
                )

            QtCore.QCoreApplication.processEvents()

            # get the current pipeline config id
            sg_data_current_pc = self._bundle.shotgun.find_one(
                "PipelineConfiguration",
                [["id", "is", self._bundle.sgtk.pipeline_configuration.get_shotgun_id()]],
                ["project", "plugin_ids"]
            )

            QtCore.QCoreApplication.processEvents()

            descriptor_uri = "sgtk:descriptor:dev?path=%s" % urllib.quote(path)

            # ok we are good to go!
            self._bundle.shotgun.create(
                "PipelineConfiguration",
                {
                    "code": self.ui.config_name.text(),
                    "plugin_ids": sg_data_current_pc["plugin_ids"],  # inherit from source config
                    "project": sg_data_current_pc["project"],  # inherit from source config
                    "descriptor": descriptor_uri
                }
            )

            QtCore.QCoreApplication.processEvents()

        except Exception, e:
            # failure
            self._overlay.show_error_message("An error was reported: %s" % e)
        else:
            # success - show tick screen
            self.ui.stackedWidget.setCurrentIndex(1)

        finally:
            # change button to close button
            self.ui.action_button.setText("Close")
            self.ui.action_button.clicked.connect(self.close)
