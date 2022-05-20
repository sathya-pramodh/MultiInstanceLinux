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
import keyboard
import macro_handlers.instance_switch_handler as switch_macro
import macro_handlers.rsg_reset_macro as reset_macro
import config
import subprocess


def get_open_instances():
    """
    Gets the open Minecraft instances by executing the command "wmctrl -l".

    Returns the list of open Minecraft instances and their full names.
    """
    instances = []
    open_windows = subprocess.check_output(["wmctrl", "-l"]).decode("UTF-8").split("\n")
    for window in open_windows:
        if window.find("Minecraft") != -1:
            instances.append(window)

    print("Debug Info: Instance names have been stored.")
    return instances


def get_hex_codes():
    """
    Gets the hex codes of the open Minecraft instances by executing the command "wmctrl -l".

    Returns the list of hex codes.
    """
    processes = subprocess.check_output(["wmctrl", "-l"]).decode("UTF-8").split("\n")
    hex_codes = []
    for process in processes:
        if process.find("Minecraft") != -1:
            hex_codes.append(process.split()[0])

    print("Debug Info: Hex codes of the windows obtained.")
    return hex_codes


def handle_instance_keybinds(instances, hex_codes):
    """
    Handles the instance keybinds defined in config.py.

    instances
        A list of all open instances as strings.
    hex_codes
        A list of the corresponding hex codes of the open instances.

    Returns None
    """
    instance_keybinds = config.SWITCH_INSTANCES
    reset_keybinds = config.RESET_ALL_INSTANCES
    while True:
        for instance_keybind in instance_keybinds:
            if keyboard.is_pressed(instance_keybind):
                switch_macro.switch_macro(
                    instance_keybinds, instances, instance_keybind, hex_codes
                )
                print("Debug Info: Switched to respective instance.")

        for reset_keybind in reset_keybinds:
            if keyboard.is_pressed(reset_keybind):
                reset_macro.reset_macro(hex_codes)
                print("Debug Info: All instances reset.")


def main():
    """
    The main function to be called for the execution of the script.

    Returns 0 if the script was executed successfully else -1 for any configuration error.
    """
    try:
        if config.NUM_INSTANCES > 9 or config.NUM_INSTANCES < 2:
            print(
                "The number of instances is < 2 or > 9. Please make necessary changes to the config file."
            )
            return -1

        open_instances = get_open_instances()
        hex_codes = get_hex_codes()

        if len(open_instances) != config.NUM_INSTANCES:
            print(
                "Some instances are not open. Please check if your instances are open."
            )
            return -1

        handle_instance_keybinds(open_instances, hex_codes)
    except KeyboardInterrupt:
        return 0


# Checking if the script has been imported from an external script.
if __name__ == "__main__":
    return_code = main()

    # Printing proper debug info based on the return code.
    if return_code == 0:
        print("Debug Info: Script exitted successfully.")
    elif return_code == -1:
        print("Debug Info: Error occured in script. Exitting...")
