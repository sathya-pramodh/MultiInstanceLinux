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
import sys
import keyboard
import macro_handlers.instance_handlers as switch_macro
import macro_handlers.reset_handlers as reset_macro
import macro_handlers.suspend_handlers as suspend_macro
import macro_handlers.wall_handlers as wall_macro
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

    Returns the dictionary of the process IDs
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


def get_obs_hex_code():
    """
    Gets the hex code of the open OBS studio window(including the spotlight window).

    Returns the hex code as a string if the window is open, else None.
    """
    processes = subprocess.check_output(["wmctrl", "-l"]).decode("UTF-8").split("\n")
    for process in processes:
        if process.find("OBS") != -1 and not config.USING_PROJECTOR:
            return process.split()[0]
        if process.find("Fullscreen Projector") != -1 and config.USING_PROJECTOR:
            return process.split()[0]

    else:
        return None


def handle_instance_keybinds(
    instance_keybinds, instance_reset_keybinds, hex_codes, pids, performance_mode
):
    """
    This is the function that handles the instance keybinds.

    instance_keybinds
    The list of keybinds to switch to a particular instance as strings.

    instance_reset_keybinds
    The list of keybinds to reset the current instance in focus as strings.

    hex_codes
    The list of hex codes of the open Minecraft instances.

    pids
    The dictionary of process IDs of the open Minecraft instances.

    performance_mode
    The string that represents the performance mode being used.

    Returns True and the instance number if the user has switched to an instance without resetting the active instance,
    else returns False and 0.
    """
    for instance_keybind in instance_keybinds:
        if keyboard.is_pressed(instance_keybind):
            hex_code, instance_number = switch_macro.instance_switch_macro(
                instance_keybinds,
                instance_keybind,
                hex_codes,
                pids,
                performance_mode,
            )
            logger.log("Switched to instance with hex code: {}".format(hex_code))
            return True, instance_number
    for instance_reset_keybind in instance_reset_keybinds:
        if keyboard.is_pressed(instance_reset_keybind):
            hex_code = switch_macro.instance_reset_macro(
                instance_reset_keybinds, instance_reset_keybind, hex_codes, pids
            )
            logger.log(
                "All instances other than the instance with hex code: {} were reset.".format(
                    hex_code
                )
            )
            return False, 0
    return False, 0


def handle_reset_keybinds(reset_all_keybinds, reset_one_keybinds, hex_codes, pids):
    """
    This is the function that handles the reset keybinds.

    reset_all_keybinds
    The list of keybinds to reset all open instances as strings.

    reset_one_keybinds
    The list of keybinds to reset the current open instance as strings.

    hex_codes
    The list of hex codes of the open Minecraft instances as strings.

    pids
    The dictionary of the process IDs of the open Minecraft instances.

    Returns True if any instance was reset, else False.
    """
    for reset_all_keybind in reset_all_keybinds:
        if keyboard.is_pressed(reset_all_keybind):
            reset_macro.reset_all_macro(hex_codes, pids)
            logger.log("All instances were reset.")
            return True

    for reset_one_keybind in reset_one_keybinds:
        if keyboard.is_pressed(reset_one_keybind):
            hex_code = reset_macro.reset_current_macro()
            logger.log("Instance with hex code: {} was reset.".format(hex_code))
            return True

    return False


def handle_suspend_keybinds(suspend_all_keybinds, pids):
    """
    This is the function that handles the suspend keybinds.

    suspend_all_keybinds
    The list of the keybinds to suspend all instances as strings.

    pids
    The dictionary of the process IDs of the open Minecraft instances.

    Returns None
    """
    for suspend_all_keybind in suspend_all_keybinds:
        if keyboard.is_pressed(suspend_all_keybind):
            hex_code = suspend_macro.suspend_all_macro(pids)
            logger.log(
                "All instances other than the instance with hex code: {} were suspended.".format(
                    hex_code
                )
            )


def handle_unsuspend_keybinds(unsuspend_all_keybinds, pids):
    """
    This is the function that handles the unsuspend keybinds.

    unsuspend_all_keybinds
    The list of the keybinds to unsuspend all instances as strings.

    pids
    The dictionary of the process IDs of the open Minecraft instances.

    Returns None
    """
    for unsuspend_all_keybind in unsuspend_all_keybinds:
        if keyboard.is_pressed(unsuspend_all_keybind):
            suspend_macro.unsuspend_all_macro(pids)
            logger.log("All instances were unsuspended.")


def handle_wall_keybinds(
    switched_to_instance_without_resetting,
    has_reset,
    instance_number,
    obs_hex_code,
    host,
    port,
    password,
    wall_scene_name,
):
    """
    This is the function that handles the wall keybinds.

    switched_to_instance_without_resetting
    The boolean which signifies whether the user has switched to an instance without resetting anything else.

    has_reset
    The boolean which signifies whether the user has reset one or more instances.

    instance_number
    The integer instance number of the instance that the user switched to. Equal to zero when the first parameter is False.

    obs_hex_code
    The hex code of the OBS studio window as a string.

    host
    The hostname of the OBS websocket server.

    port
    The port to connect to the OBS websocket server.

    password
    The password to be used to connect to the OBS websocket server.

    wall_scene_name
    The name of the wall scene on OBS as a string.

    Returns None if the code was executed successfully, else -1
    """
    if switched_to_instance_without_resetting:
        instance_name = config.INSTANCE_SCENE_NAMES[instance_number]
        return_code = wall_macro.wall_switch_macro(
            "",
            config.WEBSOCKET_HOST,
            config.WEBSOCKET_PORT,
            config.WEBSOCKET_PASSWORD,
            instance_name,
            switch_to_wall=False,
        )
        if return_code == -1:
            logger.log(
                "Couldn't find instance named '{}' in the list of scenes.".format(
                    instance_name
                )
            )
            return -1
        logger.log("Switched to instance and OBS on scene '{}'.".format(instance_name))
    elif has_reset:
        return_code = wall_macro.wall_switch_macro(
            obs_hex_code,
            config.WEBSOCKET_HOST,
            config.WEBSOCKET_PORT,
            config.WEBSOCKET_PASSWORD,
            wall_scene_name,
        )
        if return_code == -1:
            logger.log(
                "Could not find the scene '{}' in the list of scenes.".format(
                    wall_scene_name
                )
            )
            return -1
        logger.log("Switched to OBS studio on scene '{}'.".format(wall_scene_name))
    else:
        switch_to_wall_keybinds = config.SWITCH_TO_WALL
        for switch_to_wall_keybind in switch_to_wall_keybinds:
            if keyboard.is_pressed(switch_to_wall_keybind):
                if obs_hex_code is None:
                    return -1
                return_code = wall_macro.wall_switch_macro(
                    obs_hex_code, host, port, password, wall_scene_name
                )
                if return_code == -1:
                    logger.log(
                        "Could not find the scene '{}' in the list of scenes.".format(
                            wall_scene_name
                        )
                    )
                    return -1
                logger.log(
                    "Switched to OBS Studio on scene '{}'.".format(wall_scene_name)
                )


def handle_keybinds(hex_codes, obs_hex_code, pids):
    """
    Handles the keybinds defined in config.py.

    hex_codes
    A list of the corresponding hex codes of the open instances.

    obs_hex_code
    The hex code of the open OBS window as a string.

    pids
    A dictionary of the pids of the open instances.

    Returns None if the script executed successfully, else -1 for any errors.
    """
    using_wall = config.USING_WALL
    config.INSTANCE_SCENE_NAMES = config.INSTANCE_SCENE_NAMES[: len(hex_codes)]
    config.SWITCH_INSTANCES = config.SWITCH_INSTANCES[: len(hex_codes)]
    config.SWITCH_AND_RESET_INSTANCES = config.SWITCH_AND_RESET_INSTANCES[
        : len(hex_codes)
    ]
    while True:
        (
            switched_to_instance_without_resetting,
            instance_number,
        ) = handle_instance_keybinds(
            config.SWITCH_INSTANCES,
            config.SWITCH_AND_RESET_INSTANCES,
            hex_codes,
            pids,
            config.PERFORMANCE_MODE,
        )
        has_reset = handle_reset_keybinds(
            config.RESET_ALL_INSTANCES, config.RESET_CURRENT_INSTANCE, hex_codes, pids
        )
        handle_suspend_keybinds(config.SUSPEND_ALL_INSTANCES, pids)
        handle_unsuspend_keybinds(config.UNSUSPEND_ALL_INSTANCES, pids)

        if using_wall:
            return_code = handle_wall_keybinds(
                switched_to_instance_without_resetting,
                has_reset,
                instance_number,
                obs_hex_code,
                config.WEBSOCKET_HOST,
                config.WEBSOCKET_PORT,
                config.WEBSOCKET_PASSWORD,
                config.WALL_SCENE_NAME,
            )
            if return_code == -1:
                return -1


def start():
    """
    The function to be called to start the macro

    Returns 0 if the script was executed successfully else -1 for any configuration error.
    """
    try:
        hex_codes = get_hex_codes()
        logger.log("Hex codes of the windows obtained. Hex Codes: {}".format(hex_codes))
        pids = get_process_ids(hex_codes)
        logger.log("PIDs of the windows obtained. PIDs: {}".format(pids))
        obs_hex_code = get_obs_hex_code()
        logger.log("Hex code of OBS window obtained. Hex Code: {}".format(obs_hex_code))
        if len(hex_codes) == 0:
            logger.log("No Minecraft instances detected.")
            return -1
        return_code = handle_keybinds(hex_codes, obs_hex_code, pids)
        if return_code == -1:
            return return_code
    except KeyboardInterrupt:
        return 0


def get_config(project_root, config_dir):
    """
    The function to copy the default configuration file to the user's config directory.

    project_root
    The root directory of the project represented as a string.

    config_dir
    The .config directory of the user represented as a string.

    Returns None.
    """
    config_file = project_root + "/default_config.py"
    target_file = config_dir + "/MultiInstanceLinux/config.py"
    os.system("cp {} {}".format(config_file, target_file))


def main(project_root):
    """
    The main function to be called to startup the script.

    project_root
    The directory of the project root represented as a string.

    Returns None.
    """
    script_start_time = time.time()
    username = os.environ.get("SUDO_USER", os.environ.get("USERNAME"))
    if username is None:
        print(
            "Not a sudo user or no sudo user has logged in. Execute the script with sudo previleges. Exitting the script..."
        )
        return -1
    home = os.path.expanduser("~{}".format(username))
    config_dir = home + "/.config"
    log_dir = home + "/.config/MultiInstanceLinux"
    if not os.path.isdir("{}/logs/".format(log_dir)):
        if not os.path.isdir(log_dir):
            os.mkdir(log_dir)
        os.mkdir("{}/logs/".format(log_dir))
    global logger
    logger = Logging("{}/logs/".format(log_dir))
    sys.path.append(log_dir)
    if not os.path.isfile(config_dir + "/MultiInstanceLinux/config.py"):
        get_config(project_root, config_dir)
    global config
    import config

    os.chdir(project_root)
    return_code = start()

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
