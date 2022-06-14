"""
This is a helper script that handles the suspend keybinds.
Called from handle_instance_keybinds() in multi_instance.py
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
import os
import subprocess


def suspend_all_macro(pids):
    """
    The function that handles suspending all instances other than the current active instance.

    pids
    A list of the PIDs of all the open instances.

    Returns the hex code of the current active instance for logging purposes.
    """
    current_hex_code_in_base_ten = subprocess.check_output(
        ["xdotool", "getwindowfocus"]
    ).decode("UTF-8")
    current_hex_code = hex(int(current_hex_code_in_base_ten))
    if len(current_hex_code.split("x")[1]) == 7:
        current_hex_code = (
            current_hex_code.split("x")[0] + "x0" + current_hex_code.split("x")[1]
        )
    for hex_code, pid in pids.items():
        if hex_code != current_hex_code:
            os.system("kill -STOP " + pid)

    return current_hex_code


def unsuspend_all_macro(pids):
    """
    The function that handles unsuspending all instances other than the current active instance.

    pids
    A list of PIDs of all the open instances.

    Returns the hex code of the current active instance for logging purposes.
    """
    for hex_code, pid in pids.items():
        os.system("kill -CONT " + pid)
