# Copyright (c) 2017 Shotgun Software Inc.
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
        pipeline_config_id = self.sgtk.pipeline_configuration.get_shotgun_id()

        if not pipeline_config_id:
            # old configs can be bare
            return

        sg_data = self.shotgun.find_one(
            "PipelineConfiguration",
            [["id", "is", pipeline_config_id]],
            ["windows_path", "linux_path", "mac_path"]
        )

        if sg_data and (sg_data["windows_path"] or sg_data["mac_path"] or sg_data["linux_path"]):
            # centralized config - no devtools for those!
            return

        # certain menu options are only available if you
        # are running out of a dev descriptor config:
        if self.sgtk.configuration_descriptor.is_dev() or True:

            # command to jump to the dev area.
            menu_options = {
                "short_name": "jump_to_sandbox",
                "description": "Opens a file browser pointing at your dev sandbox.",
                "type": "context_menu",
            }
            self.engine.register_command(
                "Jump to config sandbox",
                self._jump_to_dev_area,
                menu_options
            )

            # command to check for updates
            menu_options = {
                "short_name": "check_updates",
                "description": "Check for app and engine updates.",
                "type": "context_menu",
            }
            self.engine.register_command(
                "Check for updates...",
                self._updates,
                menu_options
            )

        # command to create a dev sandbox
        menu_options = {
            "short_name": "new_config_sandbox",
            "description": "Create a pipeline configuration which can be used for development.",
            "type": "context_menu",
        }
        self.engine.register_command(
            "New config sandbox...",
            self._new_config,
            menu_options
        )

    def _updates(self):

        check_updates = self.import_module("check_updates")
        check_updates.show_dialog(self)


    def _new_config(self):

        create_sandbox = self.import_module("create_sandbox")
        create_sandbox.show_dialog(self)

    def _jump_to_dev_area(self):
        """
        Open a OS file manager and point it at the dev area.
        """
        disk_location = self.sgtk.configuration_descriptor.get_path()

        if sys.platform.startswith("linux"):
            cmd = 'xdg-open "%s"' % disk_location
        elif sys.platform == "darwin":
            cmd = 'open "%s"' % disk_location
        elif sys.platform == "win32":
            cmd = 'cmd.exe /C start "Folder" "%s"' % disk_location
        else:
            raise RuntimeError("Platform '%s' is not supported." % sys.platform)

        exit_code = os.system(cmd)
        if exit_code != 0:
            logger.error("Failed to launch '%s'!", cmd)

    @property
    def context_change_allowed(self):
        """
        Specifies that context changes are allowed.
        """
        return True

    def destroy_app(self):
        """
        Tear down the app
        """
        self.log_debug("Destroying tk-multi-publish2")
