# Copyright (c) 2018 Shotgun Software Inc.
#
# CONFIDENTIAL AND PROPRIETARY
#
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights
# not expressly granted therein are reserved by Shotgun Software Inc.

import os
import sys
import sgtk

logger = sgtk.platform.get_logger(__name__)


class MultiDevUtils(sgtk.platform.Application):
    """
    App with handy developer utilities.
    """

    def init_app(self):
        """
        Called as the application is being initialized
        """
        if self.sgtk.configuration_mode != self.sgtk.DISTRIBUTED:
            # not a distributed config - no devtools
            logger.debug("Centralized config detected. No devtools will be enabled.")
            return

        # command to create a dev sandbox
        menu_options = {
            "short_name": "new_config_sandbox",
            "description": "Create a pipeline configuration which can be used for development.",
            "type": "context_menu",
        }
        self.engine.register_command(
            "New config sandbox...", self._new_config_sandbox, menu_options
        )

        # certain menu options are only available if you
        # are running out of a dev descriptor config:
        if self.sgtk.configuration_descriptor.is_dev():

            # command to jump to the dev area.
            menu_options = {
                "short_name": "open_config_location",
                "description": "Opens a file browser pointing at your dev sandbox.",
                "type": "context_menu",
            }
            self.engine.register_command(
                "Open config location on disk", self._jump_to_dev_area, menu_options
            )

            # command to check for updates
            menu_options = {
                "short_name": "check_updates",
                "description": "Check for app and engine updates.",
                "type": "context_menu",
            }
            self.engine.register_command(
                "Check for config updates...", self._updates, menu_options
            )

            # command to validate
            menu_options = {
                "short_name": "core",
                "description": "Check for core updates.",
                "type": "context_menu",
            }
            self.engine.register_command(
                "Check for core updates...", self._check_core_updates, menu_options
            )

    def _updates(self):
        """
        Callback to launch check for updates tank command
        """
        command_runner = self.import_module("command_runner")
        command_runner.show_dialog(self, "Check for Updates", "updates")

    def _check_core_updates(self):
        """
        Callback to launch the validate tank command
        """
        command_runner = self.import_module("command_runner")
        command_runner.show_dialog(self, "Check for core updates", "core")

    def _new_config_sandbox(self):
        """
        Callback to show the new config sandbox UI dialog
        """
        create_sandbox = self.import_module("create_sandbox")
        create_sandbox.show_dialog(self)

    def _jump_to_dev_area(self):
        """
        Open a OS file manager and point it at the dev area.
        """
        disk_location = self.sgtk.configuration_descriptor.get_path()
        sgtk.util.filesystem.open_file_browser(disk_location)

    @property
    def context_change_allowed(self):
        """
        Specifies that context changes are allowed.
        """
        return True
