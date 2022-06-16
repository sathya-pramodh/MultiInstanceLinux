"""
This is the main script that needs to be executed in order to run MultiInstanceLinux.

Installation and Usage instructions at:
https://github.com/sathya-pramodh/MultiInstanceLinux/
"""

# Author: sathya-pramodh
# Github: https://github.com/sathya-pramodh

# Software Licensed under the MIT License.

# License terms:

# MIT License

# Copyright (c) 2022 sathya-pramodh

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Imports
import os
import time
import keyboard
import macro_handlers.instance_handlers as switch_macro
import macro_handlers.reset_handlers as reset_macro
import macro_handlers.suspend_handlers as suspend_macro
import macro_handlers.wall_handlers as wall_macro
import config
import subprocess
from helper_scripts.logging import Logging


def get_hex_codes():
    """
    Gets the hex codes of the open Minecraft instances.

    Returns the list of hex codes
    """
    processes = subprocess.check_output(["wmctrl", "-l"]).decode("UTF-8").split("\n")
    hex_codes = []
    for process in processes:
        if process.find("Minecraft") != -1:
            hex_codes.append(process.split()[0])

    return hex_codes


def get_process_ids(hex_codes):
    """
    Gets the process IDs of the open Minecraft instances.

    Returns the list of the process IDs
    """
    pids = {}
    for hex_code in hex_codes:
        pid = (
            subprocess.check_output(["xdotool", "getwindowpid", hex_code])
            .decode("UTF-8")
            .strip()
        )
        pids[hex_code] = pid

    return pids


def handle_instance_keybinds(hex_codes, pids):
    """
    Handles the instance keybinds defined in config.py.

    hex_codes
    A list of the corresponding hex codes of the open instances.

    pids
    A dictionary of the pids of the open instances.

    Returns None
    """
    instance_keybinds = config.SWITCH_INSTANCES
    reset_all_keybinds = config.RESET_ALL_INSTANCES
    reset_one_keybinds = config.RESET_CURRENT_INSTANCE
    suspend_all_keybinds = config.SUSPEND_ALL_INSTANCES
    unsuspend_all_keybinds = config.UNSUSPEND_ALL_INSTANCES
    instance_reset_keybinds = config.SWITCH_AND_RESET_INSTANCES
    performance_mode = config.PERFORMANCE_MODE
    using_wall = (
        config.USING_WALL
        if config.USING_WALL is True or config.USING_WALL is False
        else True
    )
    while True:
        for instance_keybind in instance_keybinds:
            if keyboard.is_pressed(instance_keybind):
                hex_code = switch_macro.instance_switch_macro(
                    instance_keybinds, instance_keybind, hex_codes, pids, performance_mode
                )
                logger.log("Switched to instance with hex code: {}".format(hex_code))

        for reset_all_keybind in reset_all_keybinds:
            if keyboard.is_pressed(reset_all_keybind):
                reset_macro.reset_all_macro(hex_codes, pids)
                logger.log("All instances were reset.")

        for reset_one_keybind in reset_one_keybinds:
            if keyboard.is_pressed(reset_one_keybind):
                hex_code = reset_macro.reset_current_macro()
                logger.log("Instance with hex code: {} was reset.".format(hex_code))

        for suspend_all_keybind in suspend_all_keybinds:
            if keyboard.is_pressed(suspend_all_keybind):
                hex_code = suspend_macro.suspend_all_macro(pids)
                logger.log(
                    "All instances other than the instance with hex code: {} were suspended.".format(
                        hex_code
                    )
                )

        for unsuspend_all_keybind in unsuspend_all_keybinds:
            if keyboard.is_pressed(unsuspend_all_keybind):
                suspend_macro.unsuspend_all_macro(pids)
                logger.log("All instances were unsuspended.")

        for instance_reset_keybind in instance_reset_keybinds:
            if keyboard.is_pressed(instance_reset_keybind):
                hex_code = switch_macro.instance_reset_macro(
                    instance_reset_keybinds, instance_reset_keybind, hex_codes, pids
                )
                logger.log(
                    "All instances other than the instance with hex code: {} were reset".format(
                        hex_code
                    )
                )

        if using_wall:
            switch_to_wall_keybinds = config.SWITCH_TO_WALL
            for switch_to_wall_keybind in switch_to_wall_keybinds:
                if keyboard.is_pressed(switch_to_wall_keybind):
                    processes = (
                        subprocess.check_output(["wmctrl", "-l"])
                        .decode("UTF-8")
                        .split("\n")
                    )
                    for process in processes:
                        if process.find("OBS") != -1:
                            obs_hex_code = process.split()[0]
                            break
                    else:
                        logger.log("Could not find an open OBS studio window.")
                        return -1
                    return_code = wall_macro.wall_switch_macro(
                        obs_hex_code,
                        config.WEBSOCKET_HOST,
                        config.WEBSOCKET_PORT,
                        config.WEBSOCKET_PASSWORD,
                        config.WALL_SCENE_NAME,
                    )
                    if return_code == -1:
                        logger.log(
                            "Could not find the scene '{}' in the list of scenes.".format(
                                config.WALL_SCENE_NAME
                            )
                        )
                    logger.log(
                        "Switched to OBS Studio on scene '{}'.".format(
                            config.WALL_SCENE_NAME
                        )
                    )


def main():
    """
    The main function to be called for the execution of the script.

    Returns 0 if the script was executed successfully else -1 for any configuration error.
    """
    try:
        if config.NUM_INSTANCES > 9 or config.NUM_INSTANCES < 2:
            logger.log(
                "The number of instances should be greater than 1 and lesser than 9. Detected number of instances: {}".format(
                    config.NUM_INSTANCES
                )
            )
            return -1

        hex_codes = get_hex_codes()
        logger.log("Hex codes of the windows obtained. Hex Codes: {}".format(hex_codes))
        pids = get_process_ids(hex_codes)
        logger.log("PIDs of the windows obtained. PIDs: {}".format(pids))

        if len(hex_codes) != config.NUM_INSTANCES:
            logger.log(
                "Some instances are not open. Number of instances detected: {}".format(
                    len(hex_codes)
                )
            )
            return -1

        return_code = handle_instance_keybinds(hex_codes, pids)
        if return_code == -1:
            return return_code
    except KeyboardInterrupt:
        return 0


# Checking if the script has been imported from an external script.
if __name__ == "__main__":
    script_start_time = time.time()
    WORKING_DIRECTORY = os.getcwd()
    if not os.path.isdir("{}/log/".format(WORKING_DIRECTORY)):
        os.mkdir("{}/log/".format(WORKING_DIRECTORY))
    logger = Logging("{}/log/".format(WORKING_DIRECTORY))
    return_code = main()

    if return_code == 0:
        script_end_time = time.time()
        time_taken_by_script = script_end_time - script_start_time
        logger.log(
            "Script exitted successfully. Exitted with code 0. Time taken for execution: {} seconds".format(
                time_taken_by_script
            )
        )

    if return_code == -1:
        script_end_time = time.time()
        time_taken_by_script = script_end_time - script_start_time
        logger.log(
            "Script exitted with an error. Exitted with code -1. Time take for execution: {} seconds".format(
                time_taken_by_script
            )
        )
        print(
            "Some error occurred in the script. Please check the log files for more information. Exit code(-1)."
        )
