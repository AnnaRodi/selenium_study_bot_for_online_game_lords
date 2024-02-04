# https://habr.com/ru/articles/709314/
import time

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

    login_input = browser.find_element(By.CSS_SELECTOR, 'input.VkIdForm__input')
    login_input.send_keys(vk_cookies['phone']) #ввели номер телефона
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
    t = 50
    while t > 0:
        print('time sleep:', t)
        time.sleep(1)
        t -= 1


    # games_button = WebDriverWait(browser, 5).until_not(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/games"]'))) #так почему то не заходит
    games_button = browser.find_element(By.CSS_SELECTOR, 'a[href="/games"]')
    print('games_button: ', games_button)
    games_button.click()
    lords_button = browser.find_element(By.CSS_SELECTOR, 'div[data-title="Лорды"]')
    lords_button.click()
except Exception as entry_error:
    print(entry_error)

print('Вошли в игру')

try:
    # Store iframe web element
    iframe = browser.find_element(By.TAG_NAME, "iframe")
    print('нашли айфрейм')
    # switch to selected iframe
    browser.switch_to.frame(iframe)
    print('переключились на айфрейм')
    browser.switch_to.default_content()
    main_button = browser.find_element(By.CSS_SELECTOR, 'a[href="/Land"]')
    main_button.click()
    print('main_button clicked')
except Exception as play_error:
    print(play_error)

try:
    main_button=browser.find_element(By.CSS_SELECTOR, 'a._main')
    main_button.click()
except Exception as er:
    print(er)

try:
    button = WebDriverWait(browser, 5).until_not(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/Land"]')))
except Exception as er:
    print(er)
