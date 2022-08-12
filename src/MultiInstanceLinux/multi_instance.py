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
import subprocess
import sys
import threading
import time

import keyboard
from obswebsocket import obsws, requests

from helper_modules.logging import Logging
import script_setup


class Instance:
    """
    A Class that denotes each open instance with the necessary methods.
    """

    def __init__(
        self,
        hex_code,
        pid,
        switch_keybind,
        instance_directory,
        wall_scene_name,
    ):
        """
        hex_code
        The string denoting the hex code of the instance.

        pid
        The integer denoting the pid of the instance.

        switch_keybind
        The string that denotes the keybind to switch to this instance.

        instance_directory
        The string that denotes the absolute path to the instance directory.

        wall_scene_name
        The string denoting the name of the scene while using wall.
        """
        self.hex_code = hex_code
        self.pid = pid
        self.switch_keybind = switch_keybind
        self.instance_directory = instance_directory
        self.wall_scene_name = wall_scene_name

    def reset(self):
        """
        Method to reset the instance.
        """
        macro = "shift+Tab"
        os.system("wmctrl -i -a {}".format(self.hex_code))
        time.sleep(0.25)
        os.system("xdotool key --window {} Escape".format(self.hex_code))
        os.system("xdotool key --window {} {}".format(self.hex_code, macro))
        os.system("xdotool key --window {} Enter".format(self.hex_code))
        logger.log("Instance with hex code: '{}' has been reset.".format(self.hex_code))

    def switch(self):
        """
        Method to switch to the instance.
        """
        os.system("wmctrl -i -a {}".format(self.hex_code))
        time.sleep(0.25)
        os.system("xdotool key --window {} Escape".format(self.hex_code))
        logger.log("Switched to instance with hex code: '{}'.".format(self.hex_code))

    def handle_switch_keybind(self):
        """
        Method used by threading.Thread to handle switching to the instance.
        """
        while True:
            if keyboard.is_pressed(self.switch_keybind):
                self.switch()

    def pause_on_reload(self):
        """
        Method to pause on reload of the instance world.
        """
        paused_on_world_preview = False
        paused_on_world_load = True
        while True:
            last_line = (
                subprocess.check_output(
                    ["tail", "-n 1", self.instance_directory + "logs/latest.log"]
                )
                .decode("UTF-8")
                .strip()
            )
            if last_line[::-1][0] == "%" and not paused_on_world_preview:
                percent_world_load = int(last_line[::-1][1:3])
                if percent_world_load >= 80:
                    current_window_base_ten = subprocess.check_output(
                        ["xdotool", "getactivewindow"]
                    ).decode("UTF-8")
                    current_hex_code = hex(int(current_window_base_ten))
                    os.system("wmctrl -i -a {}".format(self.hex_code))
                    time.sleep(0.25)
                    os.system("xdotool key --window {} F3+Escape".format(self.hex_code))
                    os.system("wmctrl -i -a {}".format(current_hex_code))
                    paused_on_world_preview = True
                    paused_on_world_load = False
                    logger.log(
                        "Paused instance with hex code: '{}' on 80% world reload.".format(
                            self.hex_code
                        )
                    )

                if percent_world_load >= 95:
                    os.system("wmctrl -i -a {}".format(self.hex_code))
                    logger.log(
                        "Switched to instance with hex code: '{}' on 95% world reload.".format(
                            self.hex_code
                        )
                    )

            if (
                last_line.find("logged in with entity id") != -1
                and not paused_on_world_load
            ):
                current_window_base_ten = subprocess.check_output(
                    ["xdotool", "getactivewindow"]
                ).decode("UTF-8")
                current_window = hex(int(current_window_base_ten))
                os.system("wmctrl -i -a {}".format(self.hex_code))
                time.sleep(0.25)
                os.system("xdotool key --window {} F3+Escape".format(self.hex_code))
                os.system("wmctrl -i -a {}".format(current_window))
                paused_on_world_preview = False
                paused_on_world_load = True
                logger.log(
                    "Paused instance with hex code: '{}' on 100% world load.".format(
                        self.hex_code
                    )
                )


class Obs:
    """
    A Class that denotes the open OBS window with the necessary methods.
    """

    def __init__(self, hex_code, host, port, password, wall_keybind):
        """
        hex_code
        The string denoting the hex code of the OBS window.

        host
        The string denoting the hostname of the websocket server.

        port
        The integer denoting the open port of the websocket server.

        password
        The string denoting the password to authenticate with the websocket server.

        wall_keybind
        The string denoting the keybind to switch to the wall scene.
        """
        self.hex_code = hex_code
        self.host = host
        self.port = port
        self.password = password
        self.wall_keybind = wall_keybind

    def make_connection(self):
        """
        Method to make the connection to the websocket server.
        """
        self.con_obj = obsws(self.host, self.port, self.password)
        self.con_obj.connect()
        logger.log(
            "Connected to websocket server. Connection info: Host: {}, Port: {}".format(
                self.host, self.port
            )
        )

    def switch_to_scene(self, scene):
        """
        Method to switch to the scene named scene.

        scene
        The string denoting the name of the scene.
        """
        scene_object = self.con_obj.call(requests.GetSceneList())
        list_scenes = scene_object.datain["scenes"]
        for scenes in list_scenes:
            if scenes["name"] == scene:
                self.con_obj.call(requests.SetCurrentScene(scene))
                logger.log("Switched to scene: '{}'.".format(scene))
                return 0
        else:
            return -1

    def handle_switch_keybind(self):
        """
        Method to handle switching to the wall scene and the OBS window.
        """
        while True:
            if keyboard.is_pressed(self.wall_keybind):
                ret_code = self.switch_to_scene(config.WALL_SCENE_NAME)
                if ret_code == -1:
                    logger.log(
                        "Couldn't find the scene '{}' in the scene list".format(
                            config.WALL_SCENE_NAME
                        )
                    )
                os.system("wmctrl -i -a {}".format(self.hex_code))


def get_current_hex_code():
    """
    The function to get the hex code of the window in focus.

    Returns the string denoting the hex code.
    """
    window_id_base_ten = subprocess.check_output(["xdotool", "getwindowfocus"]).decode(
        "UTF-8"
    )
    window_hex = hex(int(window_id_base_ten))
    digits_after_x = len(window_hex.split("x")[1])
    if digits_after_x <= 7:
        window_hex = (
            window_hex.split("x")[0]
            + "x"
            + "0" * (8 - digits_after_x)
            + window_hex.split("x")[1]
        )
    return window_hex


def start():
    """
    The function to be called to start the macro

    Returns 0 if the script was executed successfully else -1 for any configuration error.
    """
    try:
        hex_codes = script_setup.get_hex_codes()
        logger.log("Hex codes of the windows obtained. Hex Codes: {}".format(hex_codes))
        pids = script_setup.get_process_ids(hex_codes)
        logger.log("PIDs of the windows obtained. PIDs: {}".format(pids))
        obs_hex_code = script_setup.get_obs_hex_code(config.USING_PROJECTOR)
        logger.log("Hex code of OBS window obtained. Hex Code: {}".format(obs_hex_code))
        if len(hex_codes) == 0:
            logger.log("No Minecraft instances detected.")
            return -1
        instances = []
        config.INSTANCE_SCENE_NAMES = config.INSTANCE_SCENE_NAMES[: len(hex_codes)]
        config.SWITCH_INSTANCES = config.SWITCH_INSTANCES[: len(hex_codes)]
        config.INSTANCE_DIRECTORIES = config.INSTANCE_DIRECTORIES[: len(hex_codes)]
        for i in range(len(hex_codes)):
            instance = Instance(
                hex_codes[i],
                pids[hex_codes[i]],
                config.SWITCH_INSTANCES[i],
                config.INSTANCE_DIRECTORIES[i],
                config.INSTANCE_SCENE_NAMES[i],
            )
            instances.append(instance)
        for instance in instances:
            switch_thread = threading.Thread(target=instance.handle_switch_keybind)
            pause_thread = threading.Thread(target=instance.pause_on_reload)
            switch_thread.start()
            pause_thread.start()

        obs = Obs(
            obs_hex_code,
            config.WEBSOCKET_HOST,
            config.WEBSOCKET_PORT,
            config.WEBSOCKET_PASSWORD,
            config.SWITCH_TO_WALL,
        )
        if config.USING_WALL:
            obs.make_connection()
        obs_thread = threading.Thread(target=obs.handle_switch_keybind)
        obs_thread.start()

        while True:
            for reset_all_keybind in config.RESET_ALL_INSTANCES:
                if keyboard.is_pressed(reset_all_keybind):
                    for instance in instances:
                        os.system("wmctrl -i -a {}".format(instance.hex_code))
                        os.system(
                            "xdotool key --window {} Escape".format(instance.hex_code)
                        )
                        instance.reset()
                        if config.USING_WALL:
                            ret_code = obs.switch_to_scene(config.WALL_SCENE_NAME)
                            if ret_code == -1:
                                logger.log(
                                    "Couldn't find the scene '{}' in the scene list.".format(
                                        config.WALL_SCENE_NAME
                                    )
                                )
                            os.system("wmctrl -i -a {}".format(obs.hex_code))

            for reset_one_keybind in config.RESET_CURRENT_INSTANCE:
                if keyboard.is_pressed(reset_one_keybind):
                    window_hex = get_current_hex_code()
                    for instance in instances:
                        if instance.hex_code == window_hex:
                            instance.reset()
                            if config.USING_WALL:
                                ret_code = obs.switch_to_scene(config.WALL_SCENE_NAME)
                                if ret_code == -1:
                                    logger.log(
                                        "Couldn't find the scene '{}' in the scene list.".format(
                                            config.WALL_SCENE_NAME
                                        )
                                    )
                                os.system("wmctrl -i -a {}".format(obs.hex_code))
                            break

            for instance_switch_keybind in config.SWITCH_INSTANCES:
                if keyboard.is_pressed(instance_switch_keybind):
                    idx = config.SWITCH_INSTANCES.index(instance_switch_keybind)
                    if config.USING_WALL:
                        ret_code = obs.switch_to_scene(config.INSTANCE_SCENE_NAMES[idx])
                        if ret_code == -1:
                            logger.log(
                                "Couldn't find instance '{}' in the scene list.".format(
                                    config.INSTANCE_SCENE_NAMES[idx]
                                )
                            )

    except KeyboardInterrupt:
        if config.USING_WALL:
            obs.con_obj.disconnect()
        return 0


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
        if not os.path.isdir(log_dir + "/config"):
            os.mkdir(log_dir + "/config")
        os.mkdir("{}/logs/".format(log_dir))
    global logger
    logger = Logging("{}/logs/".format(log_dir))
    sys.path.append(log_dir)
    if not os.path.isfile(config_dir + "/MultiInstanceLinux/config/config.py"):
        script_setup.get_config(project_root, config_dir)
    global config
    import config.config as config

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
