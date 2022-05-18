import keyboard
import time
import os


def reset_macro(instances, hex_codes):
    for hex_code in hex_codes:
        os.system("wmctrl -i -a " + hex_code)
        # time.sleep(0.1)
        # keyboard.press_and_release("Esc")
        time.sleep(0.1)
        for i in range(8):
            keyboard.press_and_release("Tab")
            time.sleep(0.1)
        keyboard.press_and_release("Return")
        time.sleep(3)
        keyboard.press_and_release("Tab")
        time.sleep(0.1)
        keyboard.press_and_release("Return")
        time.sleep(0.1)
        for i in range(3):
            keyboard.press_and_release("Tab")
            time.sleep(0.1)
        keyboard.press_and_release("Return")
        time.sleep(0.1)
        for i in range(2):
            keyboard.press_and_release("Tab")
            time.sleep(0.1)
        for i in range(3):
            keyboard.press_and_release("Return")
            time.sleep(0.1)
        for i in range(5):
            keyboard.press_and_release("Tab")
            time.sleep(0.1)
        keyboard.press_and_release("Return")
