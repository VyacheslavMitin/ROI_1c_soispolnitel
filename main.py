# Модуль выделения строк в 1С Диадок для отправки, необходимо выставить английскую раскладку на обоих машинах

# Импорты
import keyboard
import pyperclip
import time
import pyautogui as pg
from typing_unicode_str import copy_paste_text, typing_unicode_str
# from check_kassa import checking_kassa, not_nds
import check_kassa
import working_contracts

# Переменные
RANGE = 30  # количество реализация
TIMEOUT_SWITCH = 3  # пауза ожидания переключения на 1С

print(f"Необходимо переключиться в 1С в течение {TIMEOUT_SWITCH} секунд")
time.sleep(TIMEOUT_SWITCH)  # ожидание


def select_name_soispolnitel():
    pg.doubleClick(x=909, y=415)
    time.sleep(0.5)
    typing_unicode_str("Российское объединение  инкассации 63")
    time.sleep(0.5)
    pg.press('enter', presses=2, interval=0.5)
    time.sleep(0.5)


def working_documents():
    pg.press('enter')  # войти в реализцию
    time.sleep(1)
    pg.click(x=1482, y=155)
    time.sleep(0.5)
    typing_unicode_str("Соисполнитель")
    time.sleep(0.5)
    pg.press('enter')  # выбрать соисполнителя
    time.sleep(0.5)
    if check_kassa.checking_kassa() == 'Ульяновский участок пересчета':
        check_kassa.not_nds()
    time.sleep(0.5)
    select_name_soispolnitel()
    # input()
    working_contracts.paste_contract()
    time.sleep(3)
    pg.click(x=830, y=326)  # клик на кнопку заполнения филиала и договора
    time.sleep(3)
    pg.hotkey('ctrl', 'enter')  # сохранение
    time.sleep(2)
    pg.press('down')  # спуск на строку ниже
    time.sleep(0.5)
    # input()


def stepping_list():
    pg.press('left', presses=10)
    time.sleep(0.5)
    pg.press('right', presses=2)
    time.sleep(0.5)
    keyboard.press_and_release('ctrl+c')
    time.sleep(0.5)
    firt = pyperclip.paste()
    pg.press('down')
    time.sleep(0.5)
    keyboard.press_and_release('ctrl+c')
    time.sleep(0.5)
    second = pyperclip.paste()
    if firt == second:
        working_documents()
        print("Строки для обработки кончились")
        return False
    else:
        pg.press('up')
        time.sleep(0.5)
        working_documents()
        return True


if __name__ == '__main__':
    while True:
        if not stepping_list():
            break
    pg.alert("Завершено", "Завершено")  # окно об окончании