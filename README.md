# MultiInstanceLinux
Multi Instance Macro Handler for Minecraft on Linux.

# Dependencies
- keyboard (https://github.com/boppreh/keyboard)
- wmctrl (https://github.com/dancor/wmctrl)
- xdotool (https://github.com/jordansissel/xdotool)
- Atum (https://github.com/VoidXWalker/Atum)
- FastReset (https://github.com/jan-leila/FastReset/tree/1.16.1-1.4.1)

# Installation
## pip
- Debian/Debian-based distros (Ubuntu, Pop!_OS, Linux Mint, Zorin OS, etc)
```
sudo apt update
sudo apt install python-pip
```
- Arch/Arch-based distros (Manjaro, Garuda, Arco, etc)
```
sudo pacman -Sy
sudo pacman -S python-pip
```
- RHEL/RHEL-based distros (Fedora)
```
sudo dnf upgrade
sudo dnf install python-pip
```
### keyboard
```
sudo pip install keyboard
```
### wmctrl
- Debian/Debian-based distros (Ubuntu, Pop!_OS, Linux Mint, Zorin OS, etc)
```
sudo apt update
sudo apt install wmctrl
```
- Arch/Arch-based distros (Manjaro, Garuda, Arco, etc)
```
sudo pacman -Sy
sudo pacman -S wmctrl
```
- RHEL/RHEL-based distros (Fedora)
```
sudo dnf upgrade
sudo dnf intall wmctrl
```
### xdotool
- Debian/Debian-based distros (Ubuntu, Pop!_OS, Linux Mint, Zorin OS, etc)
```
sudo apt update
sudo apt install xdotool
```
- Arch/Arch-based distros (Manjaro, Garuda, Arco, etc)
```
sudo pacman -Sy
sudo pacman -S xdotool
```
- RHEL/RHEL-based distros (Fedora)
```
sudo dnf upgrade
sudo dnf install xdotool
```
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

# Default Keybinds
- `Ctrl+R` - Reset all instances (RSG)
- `Shift+R` - Reset the current instance (RSG)
- `Ctrl+1` - Switch to Instance 1
- `Ctrl+2` - Switch to Instance 2
- `Ctrl+3` - Switch to Instance 3
- `Ctrl+4` - Switch to Instance 4
- `Ctrl+5` - Switch to Instance 5
- `Ctrl+6` - Switch to Instance 6
- `Ctrl+7` - Switch to Instance 7
- `Ctrl+8` - Switch to Instance 8
- `Ctrl+9` - Switch to Instance 9

# Configuration
- All configurations can be done in config.py

## Variable Descriptions
- NUM_INSTANCES - The number of instances that you want to open.
- SWITCH_INSTANCES - The list of keybinds (in order of instance number) to switch to that respective instance.
- RESET_ALL_INSTANCES - The list of keybinds to reset all instances.
- RESET_CURRENT_INSTANCE - The list of keybinds to reset the current instance.
