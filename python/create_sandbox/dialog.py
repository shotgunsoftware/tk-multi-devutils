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
import datetime
import os
from sgtk.platform.qt import QtCore, QtGui
from tank_vendor import six

from .ui.dialog import Ui_Dialog

# import frameworks
overlay = sgtk.platform.import_framework("tk-framework-qtwidgets", "overlay_widget")

logger = sgtk.platform.get_logger(__name__)


class AppDialog(QtGui.QWidget):
    """
    Create dev sandbox dialog UI
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

        # untick copy checkbox
        self.ui.copy_config.setChecked(True)

        # spinner widget
        # now inside your app constructor, create an overlay and parent it to something
        self._overlay = overlay.ShotgunOverlayWidget(self.ui.page_input)

        # populate a default name for the sandbox
        default_name = "Config Sandbox %s" % datetime.datetime.now().strftime(
            "%Y-%m-%d"
        )
        self.ui.config_name.setText(default_name)

        self.ui.browse.clicked.connect(self._browse)
        self.ui.action_button.clicked.connect(self._process)

        self.ui.path.textChanged.connect(self._on_path_changed)

    def _on_path_changed(self):
        """
        When the path changes
        """
        path = self.ui.path.text()

        if os.path.exists(path) and len(os.listdir(path)) == 0:
            # empty folder - show option to copy config
            self.ui.copy_config.setChecked(True)
            self.ui.copy_config.setEnabled(True)
        else:
            # folder with existing content - untick copy option
            self.ui.copy_config.setChecked(False)
            self.ui.copy_config.setEnabled(False)

    def _browse(self):
        """
        Shows a file browser
        """
        dialog = QtGui.QFileDialog()
        dialog.setOption(QtGui.QFileDialog.ShowDirsOnly)
        dialog.setFileMode(QtGui.QFileDialog.Directory)
        result = dialog.exec_()
        if result == QtGui.QDialog.Accepted:
            files = dialog.selectedFiles()
            if len(files) > 0:
                path = files[0]
                self.ui.path.setText(path)

    def _process(self):
        """
        Creates a new configuration
        """
        path = six.ensure_str(self.ui.path.text())

        # validate the name
        if self.ui.config_name.text() == "":
            QtGui.QMessageBox.critical(
                self,
                "No config name specified!",
                "Please specify a name for your configuration.",
            )
            return

        # validate the path
        if path == "":
            QtGui.QMessageBox.critical(
                self,
                "No path specified!",
                "Please specify a path to your config sandbox.",
            )
            return

        # must point to an existing directory
        if not os.path.exists(path):
            QtGui.QMessageBox.critical(
                self, "Path does not exist!", "The path '%s' does not exist." % path
            )
            return

        copy_files = self.ui.copy_config.isChecked()

        # turn on progress overlay, start setting things up
        try:
            self._overlay.start_spin()
            QtCore.QCoreApplication.processEvents()

            # get the current pipeline config id
            sg_data_current_pc = self._bundle.shotgun.find_one(
                "PipelineConfiguration",
                [["id", "is", self._bundle.sgtk.configuration_id]],
                ["project", "plugin_ids"],
            )

            QtCore.QCoreApplication.processEvents()

            path_obj = sgtk.util.ShotgunPath.from_current_os_path(path)
            descriptor_uri = path_obj.as_descriptor_uri(for_development=True)

            # get the current user
            current_user_data = sgtk.util.get_current_user(self._bundle.sgtk)

            # ok we are good to go!
            logger.debug("Creating new pipeline config in ShotGrid...")
            try:
                sg_data = self._bundle.shotgun.create(
                    "PipelineConfiguration",
                    {
                        "code": self.ui.config_name.text(),
                        "users": [current_user_data] if current_user_data else None,
                        "plugin_ids": sg_data_current_pc[
                            "plugin_ids"
                        ],  # inherit from source config
                        "project": sg_data_current_pc[
                            "project"
                        ],  # inherit from source config
                        "descriptor": descriptor_uri,
                    },
                )
            except Exception as e:
                # capture the permissions error specifically and provide a better
                # error message
                if "PipelineConfiguration cannot be created by this user" in str(e):
                    raise RuntimeError(
                        "You do not have permission to create Pipeline Configurations in ShotGrid. "
                        "Please contact your site administrator."
                    )
                else:
                    # re-raise
                    raise
            else:
                logger.debug("Created %s" % sg_data)

            QtCore.QCoreApplication.processEvents()

            if copy_files:
                config_descriptor = self._bundle.sgtk.configuration_descriptor
                logger.debug(
                    "Copying config files from %r to %s" % (config_descriptor, path)
                )
                config_descriptor.copy(path)
                # delete system files
                sgtk.util.filesystem.safe_delete_folder(
                    os.path.join(path, "tk-metadata")
                )

            QtCore.QCoreApplication.processEvents()

        except Exception as e:
            # failure
            self._overlay.show_error_message("An error was reported: %s" % e)
            logger.exception("An exception was raised during sandbox creation.")
        else:
            # success - show tick screen
            self.ui.stackedWidget.setCurrentIndex(1)
        finally:
            # change button to close button
            self.ui.action_button.clicked.disconnect()
            self.ui.action_button.clicked.connect(self.close)
            self.ui.action_button.setText("Close")
