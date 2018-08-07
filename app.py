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
import sgtk
import re

logger = sgtk.platform.get_logger(__name__)


class MultiDevtools(sgtk.platform.Application):
    """
    This is the :class:`sgtk.platform.Application` subclass that defines the
    top-level publish2 interface.
    """

    def init_app(self):
        """
        Called as the application is being initialized
        """
        #tk_multi_publish2 = self.import_module("tk_multi_publish2")


        if self.sgtk.configuration_descriptor.is_dev():

            # register command
            menu_options = {
                "short_name": "jump_to_sandbox",
                "description": "Jump",
                "type": "context_menu",
            }
            self.engine.register_command(
                "Jump to config sandbox",
                self._jump_to_dev_area,
                menu_options
            )


            # register command
            menu_options = {
                "short_name": "check_updates",
                "description": "Check for updates",
                "type": "context_menu",
            }
            self.engine.register_command(
                "Check for updates",
                self._updates,
                menu_options
            )

        # register command
        menu_options = {
            "short_name": "create_new_config",
            "description": "Create ",
            "type": "context_menu",
        }
        self.engine.register_command("New config sandbox...", self._new_config, menu_options)

    def _updates(self):
        pass

    def _new_config(self):
        pass

    def _jump_to_dev_area(self):
        pass

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
