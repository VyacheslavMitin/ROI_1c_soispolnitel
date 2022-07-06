# Модуль выделения строк в 1С Диадок для отправки

# Импорты

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


for i in range(RANGE):
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
    pg.click(x=830, y=326)  # клик на кнпку заполнения филиала и договора
    time.sleep(0.5)
    pg.hotkey('ctrl', 'enter')  # сохранение
    time.sleep(2)
    pg.press('down')  # спуск на строку ниже
    time.sleep(0.5)
    # input()

pg.alert("Завершено", "Завершено")  # окно об окончании