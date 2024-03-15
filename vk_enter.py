# https://habr.com/ru/articles/709314/
import time
from pprint import pprint

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import cookies_dict
from lords_functions import take_money, go_home, do_patrol, do_taverna_meet, check_army, fight_glass_rat_raid_85
from vk_cookies import cookies_lst

# Задаем опции для Chrome
options_chrome = webdriver.ChromeOptions()
# Указываем путь к профилю пользователя
options_chrome.add_argument('user-data-dir=C:\\Users\\Анна\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1')

browser = webdriver.Chrome(options=options_chrome)
browser.implicitly_wait(10)
# открываем сайт, логинимся и переходим в игру
try:
    browser.get("https://vk.com/feed")
    #заходим в игры
    games_button = browser.find_element(By.CSS_SELECTOR, 'a[href="/games"]')
    print('games_button: ', games_button)
    games_button.click()
    #выбираем игру лорды
    lords_button = browser.find_element(By.CSS_SELECTOR, 'div[data-title="Лорды"]')
    lords_button.click()
except Exception as entry_error:
    print('не получилось войти')

print('Вошли в игру')

try:
    # Store iframe web element
    frames = browser.find_elements(By.CSS_SELECTOR, "iframe")
    # switch to selected iframe
    browser.switch_to.frame(1) #1 - это номер фрейма
    print('iframe: ', len(frames), frames)
    count_frame = 0
    for el in frames:
        print(f'count_frame {count_frame}', el.text)
except Exception as er:
    print(f'Iframe error')

count_total = 0
while True:
    do_taverna_meet(browser)
    print('ждем 3 сек')
    go_home(browser)
    print('ждем 3 сек')

    take_money(browser)
    time.sleep(3)
    print('ждем 3 сек')
    do_patrol(browser)
    time.sleep(3)
    print('ждем 3 сек')

    count_total+=1
    print('Количество пройденных циклов', count_total)

    cookies_list = browser.get_cookies()
