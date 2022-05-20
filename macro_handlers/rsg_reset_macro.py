"""
This is a helper script that handles the reset keybinds.
Called from handle_instance_keybinds in multi_instance.py
"""
# Author: sathya-pramodh
# Github: https://github.com/sathya-pramodh
# Software licensed under the MIT license.
# License Terms:

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
import keyboard
import time
import os


def reset_macro(hex_codes):
    """
    Handles the resetting macro on all instances by executing the command "wmctrl -i -a <hex_code_of_window>".
    It then executes the macro which is hardcoded for Minecraft 1.16.1.

    hex_codes
        A list of the hex codes of the open Minecraft Instances.

    Returns None
    """
    for hex_code in hex_codes:
        os.system("wmctrl -i -a " + hex_code)
        time.sleep(0.1)
        for i in range(8):
            keyboard.press_and_release("Tab")
            time.sleep(0.1)
        keyboard.press_and_release("Return")
        time.sleep(3)
        keyboard.press_and_release("Tab")
        time.sleep(0.1)
        keyboard.press_and_release("Return")
        time.sleep(0.1)
        for i in range(3):
            keyboard.press_and_release("Tab")
            time.sleep(0.1)
        keyboard.press_and_release("Return")
        time.sleep(0.1)
        for i in range(2):
            keyboard.press_and_release("Tab")
            time.sleep(0.1)
        for i in range(3):
            keyboard.press_and_release("Return")
            time.sleep(0.1)
        for i in range(5):
            keyboard.press_and_release("Tab")
            time.sleep(0.1)
        keyboard.press_and_release("Return")
