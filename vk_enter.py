# https://habr.com/ru/articles/709314/
import time
from pprint import pprint

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import vk_cookies
from lords_functions import take_money, go_home, do_patrol, do_taverna_meet

browser = webdriver.Chrome()

# открываем сайт, логинимся и переходим в игру
try:
    browser.get("https://vk.com/feed")
    browser.implicitly_wait(5)

    # вводим номер телефона
    login_input = browser.find_element(By.CSS_SELECTOR, 'input.VkIdForm__input')
    login_input.send_keys(vk_cookies['phone'])
    # жмем кнопку войти
    reg_button = browser.find_element(By.CSS_SELECTOR, 'span.FlatButton__in')
    print(reg_button.text)
    reg_button.click()
    # жмем войти другим способом
    reg_button = browser.find_element(By.CSS_SELECTOR, 'span.vkuiButton__in')
    print(reg_button.text)
    reg_button.click()
    #выбираем способ входа по паролю
    reg_button = browser.find_element(By.CSS_SELECTOR, 'div[data-test-id="verificationMethod_password"]')
    print(reg_button.text)
    reg_button.click()
    #вводим пароль
    reg_button = browser.find_element(By.CSS_SELECTOR, 'input[name="password"]')
    print(reg_button.text)
    reg_button.send_keys(vk_cookies['password'])
    # жмем кнопку
    reg_button = browser.find_element(By.CSS_SELECTOR, 'span.vkuiButton__in')
    print(reg_button.text)
    reg_button.click()
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
time.sleep(2)

#переходим во фрейм
try:
    # Store iframe web element
    frames = browser.find_elements(By.CSS_SELECTOR, "iframe")
    # switch to selected iframe
    browser.switch_to.frame(1) #1 - это номер фрейма
except Exception as er:
    print(f'Iframe error')

count_total = 0
while True:
    do_taverna_meet(browser)
    print('ждем 1 сек')
    go_home(browser)
    time.sleep(1)

    count_total+=1
    print('Количество пройденных циклов', count_total)

