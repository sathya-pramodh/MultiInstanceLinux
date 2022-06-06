"""
This is a helper script that handles the instance keybinds.
Called from handle_instance_keybinds() in multi_instance.py
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


def instance_switch_macro(instance_keybinds, keybind, hex_codes):
    """
    Handles the switch instances macro.

    instance_keybinds
        A list of keybinds as strings.
    keybind
        A string denoting the keybind pressed.
    hex_codes
        A list of the hex codes of the open Minecraft instances.

    Returns None

    """
    instance_number = instance_keybinds.index(keybind)
    target_hex_code = hex_codes[instance_number]
    current_hex_code_in_base_ten = subprocess.check_output(
        ["xdotool", "getactivewindow"]
    ).decode("UTF-8")
    current_hex_code = hex(int(current_hex_code_in_base_ten))
    os.system("wmctrl -i -a " + current_hex_code)
    time.sleep(0.25)
    os.system("xdotool key --window " + current_hex_code + " Escape")
    os.system("wmctrl -i -a " + target_hex_code)
    time.sleep(0.25)
    os.system("xdotool key --window " + target_hex_code + " Escape")
