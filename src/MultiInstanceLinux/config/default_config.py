"""
This is the default config file for MultiInstanceLinux.
"""
# Make this option True if you want to use a Wall for multi instancing.
# Also make sure that obs websocket is installed when you make this True.
# Allowed values are True, False.
# The default is False.
USING_WALL = False

# Make this False if you do not want to use a Fullscreen Projector on the WALL_SCENE_NAME scene.
# Make sure to open the projector window before starting up the script.
# Because it obtains the hex code of that window during startup.
# The default is True.
USING_PROJECTOR = True

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
# The value must adhere to the allowed values of the keyboard module, else the script will exit out with an error message.
# The allowed values of the keyboard module can be found at: https://github.com/boppreh/keyboard
# The default is "o"
SWITCH_TO_WALL = "o"

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

# The absolute paths to the directories of the instances ordered by instance number.
# Absolute paths imply the full paths. Example: /home/sampleuser/Instance1/
# If you are using MultiMC or any of its forks, it should look like this:
# "/home/<your_username>/multimc/instances/<instance_name>/minecraft/"
# Check whether the directory you are pointing to has a logs directory in it.
# This is used to pause the instance on world load.
# The default is not specified.
INSTANCE_DIRECTORIES = [""]

# The list of keybinds for resetting all instances.
# You can use multiple keys to reset the instances.
# The default is ["u"].
RESET_ALL_INSTANCES = ["u"]

# The list of keybinds for resetting the current instance in focus.
# Each element of the list must adhere to the allowed values of the keyboard module, else the script will exit out with an error message.
# The allowed values for the keyboard module can be found at: https://github.com/boppreh/keyboard
# Note: Do not use 'alt' instead of 'shift' here because the macro contains 'Tab' as a part of it and 'alt+tab' is already a keybind in most desktop environments.
# The default is ["p"]
RESET_CURRENT_INSTANCE = ["p"]
