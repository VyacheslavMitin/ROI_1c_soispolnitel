import time
import keyboard
import pyautogui as pg
import pyperclip
from typing_unicode_str import copy_paste_text, typing_unicode_str
import check_kassa

DICT_CONTRACTS = {
    '01-13-05/20/816 от 20.11.2020': 'ООО Скартел 01-13-05/20/816 инкассация от 20.11.2020',  # Скартел
    '01-09-01/619 от 25.05.2018': 'Ситилинк ООО 01-09-01/619 от 25.05.2018 (инкассация)',  # Ситилинк
    '': '',  #
    '': '',  #
    '': '',  #
    '': '',  #
    '': '',  #
    '': '',  #
    '': '',  #
    '': '',  #
    '': '',  #
    '': '',  #
    '': '',  #
    '': '',  #
}

DICT_CONTRACTS_KASSA = {
    '01-13-05/20/816 от 20.11.2020': "ООО Скартел 01-13-05/20/816 пересчет от 20.11.2020",  # СКАРТЕЛ ООО (РОИ)
    '01-09-01/619 от 25.05.2018': "Ситилинк ООО 01-09-01/619 от 25.05.2018 (пересчет)",  # Ситилинк
    'D200432298 от 25.01.2021(касса пересчета)': "АО ''Русская телефонная комп'' D200432298 от 25.01.2021 (пересчет)",  # РТК
    '01-09-01/19/155 от 19.03.2019': 'АО "Мэлон Фэшн Груп" 01-09-01/19/155 от 19.03.2019 (пересчет)',  # Мэлон
    '01-09-02/274 от 01.06.2017': 'АО "МегаФон Ритейл" (пересчет) 01-09-02/274 от 01.06.2017',  # МЕгафон
    # '': '',  #
}


def paste_contract():
    dct = {}
    clipboard_ = ''
    pg.click(x=591, y=218)  # click в поле с договором
    time.sleep(0.5)
    keyboard.press_and_release('ctrl+c')
    time.sleep(0.5)
    clipboard_ = pyperclip.paste()
    print(clipboard_)
    pg.press('esc')
    if check_kassa.checking_kassa() == 'Ульяновский участок пересчета':
        dct = DICT_CONTRACTS_KASSA
    else:
        dct = DICT_CONTRACTS
    pg.doubleClick(x=1048, y=407)
    time.sleep(0.5)
    print(dct.get(clipboard_))
    typing_unicode_str(dct.get(clipboard_))
    pg.press('enter', presses=2, interval=0.3)
