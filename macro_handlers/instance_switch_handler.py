import os


def switch_macro(instance_keybinds, instances, keybind, hex_codes):
    instance_number = instance_keybinds.index(keybind) + 1
    for child in instances:
        if child.split()[0] == hex_codes[instance_number - 1]:
            os.system("wmctrl -i -a" + str(hex_codes[instance_number - 1]))
