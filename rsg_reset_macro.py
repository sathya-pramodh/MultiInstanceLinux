import keyboard
import time


def reset_macro():
    time.sleep(0.1)
    keyboard.press_and_release("Esc")
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


keyboard.add_hotkey("ctrl+r", reset_macro)

while True:
    keyboard.wait("ctrl+r")
    time.sleep(10)
