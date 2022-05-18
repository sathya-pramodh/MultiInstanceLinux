import keyboard
import macro_handlers.instance_switch_handler as switch_macro
import macro_handlers.rsg_reset_macro as reset_macro
import config
import subprocess


def get_open_instances():
    instances = []
    open_windows = subprocess.check_output(["wmctrl", "-l"]).decode("UTF-8").split("\n")
    for window in open_windows:
        if window.find("Minecraft") != -1:
            instances.append(window)

    print("Debug Info: Instance names have been stored.")
    return instances


def get_hex_codes():
    processes = subprocess.check_output(["wmctrl", "-l"]).decode("UTF-8").split("\n")
    hex_codes = []
    for process in processes:
        if process.find("Minecraft") != -1:
            hex_codes.append(process.split()[0])

    print("Debug Info: Hex codes of the windows obtained.")
    return hex_codes


def handle_instance_keybinds(instances, hex_codes):
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
                reset_macro.reset_macro(instances, hex_codes)
                print("Debug Info: All instances reset.")


def main():
    if config.NUM_INSTANCES > 9 or config.NUM_INSTANCES < 2:
        print(
            "The number of instances is < 2 or > 9. Please change the config file to continue."
        )
        return

    open_instances = get_open_instances()
    hex_codes = get_hex_codes()

    if len(open_instances) != config.NUM_INSTANCES:
        print(
            "Some instances are not open. Please check if your instances are open to continue!"
        )
        return

    handle_instance_keybinds(open_instances, hex_codes)


if __name__ == "__main__":
    main()
