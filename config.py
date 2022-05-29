"""
This is the config file for MultiInstanceLinux.
"""

# Number of Minecraft instances that you want to run.
# Remember: The number of open instances must match this given number, else the script will fail.
# Allowed range of integers: 2 to 9 both inclusive.
# The default is 2.
NUM_INSTANCES = 2

# The list of keybinds for switching instances (in order of instance number).
# Each element of the list must adhere to the allowed values of the keyboard module, else the script will exit out with an error message.
# The allowed values for the keyboard module can be found at: https://github.com/boppreh/keyboard
# The default is [ "ctrl+Num 1", "ctrl+Num 2", "ctrl+Num 3", "ctrl+Num 4", "ctrl+Num 5", "ctrl+Num 6", "ctrl+Num 7", "ctrl+Num 8", "ctrl+Num 9" ].
SWITCH_INSTANCES = [
    "ctrl+Num 1",
    "ctrl+Num 2",
    "ctrl+Num 3",
    "ctrl+Num 4",
    "ctrl+Num 5",
    "ctrl+Num 6",
    "ctrl+Num 7",
    "ctrl+Num 8",
    "ctrl+Num 9",
]

# The list of keybinds for resetting all instances.
# You can use multiple keys to reset the instances.
# The default is ["ctrl+r"].
RESET_ALL_INSTANCES = ["ctrl+r"]

# The list of keybinds for resetting each instance (in order of instance number).
# Each element of the list must adhere to the allowed values of the keyboard module, else the script will exit out with an error message.
# The allowed values for the keyboard module can be found at: https://github.com/boppreh/keyboard
# Note: Do not use 'alt' instead of 'shift' here because the macro contains 'Tab' as a part of it and 'alt+tab' is already a keybind in most desktop environments.
# The default is ["shift+Num 1", "shift+Num 2", "shift+Num 3", "shift+Num 4", "shift+Num 5", "shift+Num 6", "shift+Num 7", "shift+Num 8", "shift+Num 9"]
RESET_INSTANCES = [
    "shift+Num 1",
    "shift+Num 2",
    "shift+Num 3",
    "shift+Num 4",
    "shift+Num 5",
    "shift+Num 6",
    "shift+Num 7",
    "shift+Num 8",
    "shift+Num 9",
]
