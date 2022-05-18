import os


def switch_macro(instance_keybinds, instances, keybind, hex_codes):
    instance_number = instance_keybinds.index(keybind) + 1
    for child in instances:
        name = child.get_wm_name()
        if name[len(name) - 1] == str(instance_number):
            os.system("wmctrl -i -a" + str(hex_codes[instance_number - 1]))
