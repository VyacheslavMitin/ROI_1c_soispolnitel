import time
import keyboard
import pyautogui as pg
import pyperclip
from typing_unicode_str import copy_paste_text, typing_unicode_str


def checking_kassa() -> bool:
    clipboard = ''
    pg.click(x=1296, y=184)  # click в поле c подразделением
    time.sleep(0.5)
    keyboard.press_and_release('ctrl+c')
    time.sleep(0.5)
    clipboard = pyperclip.paste()
    # print(clipboard)
    pg.press('esc')
    return clipboard


def not_nds():
    time.sleep(0.5)
    pg.click(x=1391, y=187)  # ставим галку что необлагаемая налогом
    time.sleep(0.5)
    pg.click(x=1447, y=232)  # кликаем в поле номер акта
    time.sleep(0.5)
    typing_unicode_str("77777")



# if checking_kassa():
#     not_nds()
