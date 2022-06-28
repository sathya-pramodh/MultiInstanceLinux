"""
This is a helper script that handles the instance keybinds.
"""

# Author: sathya-pramodh
# Github: https://github.com/sathya-pramodh/

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
import time
import os
import subprocess


def instance_switch_macro(
    instance_keybinds, keybind, hex_codes, pids, performance_mode
):
    """
    Handles the switch instances macro.

    instance_keybinds
    A list of keybinds as strings.

    keybind
    A string denoting the keybind pressed.

    hex_codes
    A list of the hex codes of the open Minecraft instances.

    pids
    A dictionary of process IDs of the open Minecraft instances.

    Returns the hex code and the instance number of the instance that was switched to for logging purposes.
    """
    instance_number = instance_keybinds.index(keybind)
    target_hex_code = hex_codes[instance_number]

    if performance_mode == "F":
        current_hex_code_in_base_ten = subprocess.check_output(
            ["xdotool", "getactivewindow"]
        ).decode("UTF-8")
        current_hex_code = hex(int(current_hex_code_in_base_ten))
        if len(current_hex_code.split("x")[1]) == 7:
            current_hex_code = (
                current_hex_code.split("x")[0] + "x0" + current_hex_code.split("x")[1]
            )
        for hex_code in hex_codes:
            if hex_code != current_hex_code and hex_code != target_hex_code:
                os.system("kill -STOP " + pids[hex_code])
        os.system("kill -CONT " + pids[target_hex_code])
    os.system("wmctrl -i -a " + target_hex_code)

    return target_hex_code, instance_number


def instance_reset_macro(instance_reset_keybinds, keybind, hex_codes, pids):
    """
    Handles the macro for resetting all other instances and switching to an instance.

    instance_reset_keybinds
    A list of keybinds as strings.

    keybind
    A string denoting the keybind pressed.

    hex_codes
    A list of the hex codes of the open Minecraft instances.

    pids
    A dictionary of process IDs of the Minecraft instances.

    Returns the hex code of the instance reset for loggging purposes
    """
    instance_number = instance_reset_keybinds.index(keybind)
    target_hex_code = hex_codes[instance_number]
    macro = " shift+Tab"
    for hex_code in hex_codes:
        if hex_code != target_hex_code:
            os.system("kill -CONT " + pids[hex_code])
            os.system("wmctrl -i -a " + hex_code)
            time.sleep(0.25)
            os.system("xdotool key --window " + hex_code + " Escape")
            os.system("xdotool key --window " + hex_code + macro)
            os.system("xdotool key --window " + hex_code + " Enter")

    os.system("wmctrl -i -a " + target_hex_code)
    return target_hex_code
