# MultiInstanceLinux
Multi Instance Macro Handler for Minecraft on Linux.

# Features
- 1.16.1 RSG support.
- Wall support.
- OBS integration for Wall Resetting.
- Full keyboard support.
- An "almost" drop-in repleacement on Linux for [Specnr's macro designed for Windows](https://github.com/Specnr/MultiResetWall)

# Dependencies
- [keyboard](https://github.com/boppreh/keyboard)
- [wmctrl](https://github.com/dancor/wmctrl)
- [xdotool](https://github.com/jordansissel/xdotool)
- [Atum](https://github.com/VoidXWalker/Atum)
- [FastReset](https://github.com/jan-leila/FastReset/tree/1.16.1-1.4.1)
- [obs-websocket-py](https://github.com/Elektordi/obs-websocket-py)
- [OBS websocket plugin](https://github.com/obsproject/obs-websocket)

# Installation
### keyboard
- Install pip on your system first to install this dependency.
```
sudo pip install keyboard
```
### wmctrl
- Debian/Debian-based distros 
```
sudo apt update
sudo apt install wmctrl
```
- Arch/Arch-based distros 
```
sudo pacman -Sy
sudo pacman -S wmctrl
```
- RHEL/RHEL-based distros 
```
sudo dnf upgrade
sudo dnf intall wmctrl
```
### xdotool
- Debian/Debian-based distros 
```
sudo apt update
sudo apt install xdotool
```
- Arch/Arch-based distros
```
sudo pacman -Sy
sudo pacman -S xdotool
```
- RHEL/RHEL-based distros
```
sudo dnf upgrade
sudo dnf install xdotool
```

### obs-websocket-py
- Download this if and only if you plan on using wall.

```
sudo pip install obs-websocket-py
```

### OBS websocket plugin
- Download this if and only if you plan on using wall.
- No need to download this if you are using OBS Studio > 28.0.0
- Binaries for OBS Studio < 28.0.0 on Debian/Debian-based distros are available in the [releases](https://github.com/obsproject/obs-websocket/releases) tab of the websocket repository.
- flatpak
```
flatpak install com.obsproject.Studio.Plugin.WebSocket  
```
- Arch/Arch-based distros - Using [yay](https://github.com/Jguer/yay)
```
yay -Sy
yay -S obs-websocket
```
- Note: The script was tested on 'obs-studio-tytan652' available on the AUR (Arch User Repositories).
- Any bugs on other versions can be posted in the [Issues](https://github.com/sathya-pramodh/MultiInstanceLinux/issues) tab.

## Download the latest release from the releases page

## Extract the .zip or .tar.gz file and then follow the usage instructions

## Dev Instructions
- Clone this repository
```
git clone https://github.com/sathya-pramodh/MultiInstanceLinux
cd MultiInstanceLinux/
```
- Update your local repository
```
git pull origin main
```

# Usage
- This command must be executed in a terminal each time you want to use the macro. You could set it up so that the script runs each time you start up all the instances of Minecraft.
```
sudo python3 multi_instance.py
```

## Some important instructions
- This macro also assumes that you are using Atum and FastReset mods for Minecraft 1.16.1. It is hardcoded assuming so.
- Use all your instances in 'windowed' mode as using it in fullscreen minimizes the Minecraft window as you switch to OBS while using wall.
- If you do not want to use wall resetting, make sure to set the same keybinds as the macro to switch instances and to switch scenes. For example, in the default config, one would have to set `Ctrl+1` to switch to the instance named "Instance 1" in OBS.
- Log files are located in the 'log' directory in the project script's main folder. So, issues must be submitted with the relevant log files attached to them.
- The 'testing' branch is meant only for testing purposes and releases from that branch are created with the '-testing' tag at the end of them.

# Contribution
- Code contributions can be made to the testing branch. Pull requests must be made with proper comments and documentation.
- The code must follow all PEP8 conventions and must be in python3.x ONLY.

# Default Keybinds
- `Ctrl+R` - Reset all instances (RSG)
- `Shift+R` - Reset the current instance (RSG)
- `Ctrl+S` - Suspend all instances other than the active one.
- `Alt+S` - Unsuspend all instances.
- `Ctrl+o` - Switch to the wall scene on OBS (Only while using wall).
- `Ctrl+1` - Switch to Instance 1
- `Ctrl+2` - Switch to Instance 2
- `Ctrl+3` - Switch to Instance 3
- `Ctrl+4` - Switch to Instance 4
- `Ctrl+5` - Switch to Instance 5
- `Ctrl+6` - Switch to Instance 6
- `Ctrl+7` - Switch to Instance 7
- `Ctrl+8` - Switch to Instance 8
- `Ctrl+9` - Switch to Instance 9
- `Shift+1` - Switch to Instance 1 and reset all others.
- `Shift+2` - Switch to Instance 2 and reset all others.
- `Shift+3` - Switch to Instance 3 and reset all others.
- `Shift+4` - Switch to Instance 4 and reset all others.
- `Shift+5` - Switch to Instance 5 and reset all others.
- `Shift+6` - Switch to Instance 6 and reset all others.
- `Shift+7` - Switch to Instance 7 and reset all others.
- `Shift+8` - Switch to Instance 8 and reset all others.
- `Shift+9` - Switch to Instance 9 and reset all others.

# Configuration
- All configurations can be done in config.py

## Variable Descriptions
- USING_WALL - Option to use Wall for multi instancing.
- USING_PROJECTOR - Option to use OBS Projector while using wall.
- WEBSOCKET_HOST - The hostname of the websocket server.
- WEBSOCKET_PORT - The port on the host where the server is hosted.
- WEBSOCKET_PASSWORD - The password that is set to connect to the websocket server.
- WALL_SCENE_NAME - The name of the wall scene on OBS.
- SWITCH_TO_WALL - The list of keybinds to switch to the wall scene on OBS.
- INSTANCE_SCENE_NAMES - The list of scene names (in order of instance number) on OBS.
- PERFORMANCE_MODE - The performance enhancement option while multi instancing.
- NUM_INSTANCES - The number of instances that you want to open.
- SWITCH_INSTANCES - The list of keybinds (in order of instance number) to switch to that respective instance.
- SWITCH_AND_RESET_INSTANCES - The list of keybinds (in order of instance number) to reset all other instances and switch to an instance.
- RESET_ALL_INSTANCES - The list of keybinds to reset all instances.
- RESET_CURRENT_INSTANCE - The list of keybinds to reset the current instance.
- SUSPEND_ALL_INSTANCES - The list of keybinds for suspending instances other than the active instance.
- UNSUSPEND_ALL_INSTANCES - The list of keybinds for un-suspending all instances.
