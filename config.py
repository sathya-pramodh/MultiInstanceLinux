"""
This is the config file for MultiInstanceLinux.
"""
# Make this option True if you want to use a Wall for multi instancing.
# Also make sure that obs websocket is installed when you make this True.
# Allowed values are True, False.
# The default is False.
USING_WALL = False

# The hostname of the websocket server.
# Should be given as a string ONLY.
# The default is "localhost".
WEBSOCKET_HOST = "localhost"

# The port on WEBSOCKET_HOST where the server is hosted.
# Should be given as an integer ONLY.
# The default is 4444.
WEBSOCKET_PORT = 4444

# The password that is set to connect to the websocket server.
# DO NOT SHARE THIS PASSWORD WITH ANYONE!
# The password should be given as a string ONLY.
# Ex: WEBSOCKET_PASSWORD = "password"
# It is highly recommended that you change this password from default in OBS.
# The default is "changeme".
WEBSOCKET_PASSWORD = "changeme"

# The name of the wall scene on OBS.
# Should be given as a string ONLY.
# The default is "Verification".
WALL_SCENE_NAME = "Verification"

# The list of keybinds to switch to the wall, i.e, switch to OBS on the 'WALL_SCENE_NAME' scene.
# Each element of the list must adhere to the allowed values of the keyboard module, else the script will exit out with an error message.
# The allowed values of the keyboard module can be found at: https://github.com/boppreh/keyboard
# The default is ["ctrl+o"]
SWITCH_TO_WALL = ["ctrl+o"]

# The list of names of the scenes (in order of instance number).
# Be very careful while listing these names.
# They must perfectly match the scene names on OBS.
# The default is ["Instance 1", "Instance 2", "Instance 3", "Instance 4", "Instance 5", "Instance 6", "Instance 7", "Instance 8", "Instance 9"]
INSTANCE_SCENE_NAMES = [
    "Instance 1",
    "Instance 2",
    "Instance 3",
    "Instance 4",
    "Instance 5",
    "Instance 6",
    "Instance 7",
    "Instance 8",
    "Instance 9",
]

# This is a performance option.
# Allowed values are "F","N" and "".
# "F" - Auto suspend on switching instances.
# "N" and "" - Do not use any performance optimization.
# The default is "N".
PERFORMANCE_MODE = "N"

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

# The list of keybinds for switching to a particular instance and resetting all other instances.
# Each element of the list must adhere to the allowed values of the keyboard module, else the script will exit out with an error message.
# The allowed values of the keyboard module can be found at: https://github.com/boppreh/keyboard
# The default is ["shift+1", "shift+2", "shift+3", "shift+4", "shift+5", "shift+6", "shift+7", "shift+8", "shift+9"]
SWITCH_AND_RESET_INSTANCES = [
    "shift+1",
    "shift+2",
    "shift+3",
    "shift+4",
    "shift+5",
    "shift+6",
    "shift+7",
    "shift+8",
    "shift+9",
]

# The list of keybinds for resetting all instances.
# You can use multiple keys to reset the instances.
# The default is ["ctrl+r"].
RESET_ALL_INSTANCES = ["ctrl+r"]

# The list of keybinds for resetting the current instance in focus.
# Each element of the list must adhere to the allowed values of the keyboard module, else the script will exit out with an error message.
# The allowed values for the keyboard module can be found at: https://github.com/boppreh/keyboard
# Note: Do not use 'alt' instead of 'shift' here because the macro contains 'Tab' as a part of it and 'alt+tab' is already a keybind in most desktop environments.
# The default is ["shift+r"]
RESET_CURRENT_INSTANCE = ["shift+r"]

# The list of keybinds for suspending instances other than the active instance.
# Each element of the list must adhere to the allowed values of the keyboard module, else the script will exit out with an error message.
# The allowed values of the keyboard module can be found at: https://github.com/boppreh/keyboard
# The default is ["ctrl+s"]
SUSPEND_ALL_INSTANCES = ["ctrl+s"]

# The list of keybinds for un-suspending all instances.
# Each element of the list must adhere to the allowed values of the keyboard module, else the script will exit out with an error message.
# The allowed values of the keyboard module can be found at: https://github.com/boppreh/keyboard
# The default is ["alt+s"]
UNSUSPEND_ALL_INSTANCES = ["alt+s"]
