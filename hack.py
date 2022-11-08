import pyautogui
import keyboard

while True:
    mana_and_hp = (30, 30, 30)

    # HP
    if pyautogui.pixel(576, 1049) == mana_and_hp:
        keyboard.send("Q")

    # MANA
    elif pyautogui.pixel(1307, 1049) == mana_and_hp:
        keyboard.send("E")
