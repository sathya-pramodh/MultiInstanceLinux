# MultiInstanceLinux
Multi Instance Macro Resetter for Linux.

# Dependencies
- keyboard (https://github.com/boppreh/keyboard)
- wmctrl  (Installed on all Linux systems by default)
- python-xlib

# Installation
## Dependencies
Dependencies are installed with sudo, because keyboard requires sudo in order to run on Linux.
```
sudo pip install keyboard python-xlib
```
## Run the Script
```
git clone https://github.com/sathya-pramodh/MultiInstanceLinux
cd MultiInstanceLinux/
sudo python3 multi_instance.py
```

# Default Keybinds
- Ctrl+R - Reset all instances (RSG)
- Ctrl+1 - Switch to Instance 1
- Ctrl+2 - Switch to Instance 2
- Ctrl+3 - Switch to Instance 3
- Ctrl+4 - Switch to Instance 4
- Ctrl+5 - Switch to Instance 5
- Ctrl+6 - Switch to Instance 6
- Ctrl+7 - Switch to Instance 7
- Ctrl+8 - Switch to Instance 8
- Ctrl+9 - Switch to Instance 9

# Configuration
All configuration can be done in config.py
## Variable Descriptions
- NUM_INSTANCES - The number of instances that you want to open.
- SWITCH_INSTANCES - The list of keybinds (in order of instance number) to switch to that respective instance.
- RESET_ALL_INSTANCES - The list of keybinds to reset all instances.

# This repository is in alpha, any issues can be posted under the issues tab.
