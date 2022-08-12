"""
This is the setup script for MultiInstanceLinux.
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


def get_obs_hex_code(using_projector):
    """
    Gets the hex code of the open OBS studio window(including the spotlight window).

    using_projector
    A boolean value determining if the user is using OBS Projector Scene.

    Returns the hex code as a string if the window is open, else None.
    """
    processes = subprocess.check_output(["wmctrl", "-l"]).decode("UTF-8").split("\n")
    for process in processes:
        if process.find("OBS") != -1 and not using_projector:
            return process.split()[0]
        if process.find("Fullscreen Projector") != -1 and using_projector:
            return process.split()[0]

    else:
        return None


def get_config(project_root, config_dir):
    """
    The function to copy the default configuration file to the user's config directory.

    project_root
    The root directory of the project represented as a string.

    config_dir
    The .config directory of the user represented as a string.

    Returns None.
    """
    config_file = project_root + "/config/default_config.py"
    target_file = config_dir + "/MultiInstanceLinux/config/config.py"
    os.system("cp {} {}".format(config_file, target_file))
