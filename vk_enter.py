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

test_el = browser.find_element(By.TAG_NAME, 'html')
info = test_el.text
print(f'текст в элементе html до фрейма: ', test_el.text, '\n',
              'frame attr: ', test_el.__dict__, '\n',
              'tag_name: ', test_el.tag_name, '\n',       #tag_name:  iframe
               'location ', test_el.location, '\n',       #location  {'x': 0, 'y': -19}
               'id ', test_el.id )                        #id  B9EF7451B8ACA33C1D9362E2649F14DA_element_153
i=1
try:
    # Store iframe web element
    frames = browser.find_elements(By.CSS_SELECTOR, "iframe")
    ''' for frame in frames:
        print(f'нашли айфрейм в цикле{i}', frame, '\n', #<selenium.webdriver.remote.webelement.WebElement (session="3de9f0e31bad5d04a19fb44e2b477acb",
                                                        # element="B9EF7451B8ACA33C1D9362E2649F14DA_element_153")>
              'frame attr: ', frame.__dict__, '\n',     # frame attr:  {'_parent': <selenium.webdriver.chrome.webdriver.WebDriver (session="3de9f0e31bad5d04a19fb44e2b477acb")>,
                                                        # '_id': 'B9EF7451B8ACA33C1D9362E2649F14DA_element_153'}
              'tag_name: ', frame.tag_name, '\n',       #tag_name:  iframe
               'location ', frame.location, '\n',       #location  {'x': 0, 'y': -19}
               'id ', frame.id, '\n',                         #id  B9EF7451B8ACA33C1D9362E2649F14DA_element_153
               'text', frame.text)
        print('browser.title', browser.title)
        print('browser.current_url', browser.current_url)'''

    # switch to selected iframe
    browser.switch_to.frame(i)
    print(f'переключились на айфрейм цикл {i}')
    print('browser.title', browser.title)
    print('browser.current_url', browser.current_url)
    print('time sleep')
    time.sleep(5)
    dives = browser.find_elements(By.TAG_NAME, "div")
    land_button = browser.find_element(By.ID, 'menu-fields')
    land_button.click()
    print('land_button is clicked. time sleep')
    time.sleep(5)
    '''dives = browser.find_elements(By.TAG_NAME, "div")
    for d in dives:
        print(f'нашли div в цикле{i}', d, '\n',
              'div attr: ', d.__dict__, '\n',
              'tag_name: ', d.tag_name, '\n',  # tag_name:  iframe
              'location ', d.location, '\n',  # location  {'x': 0, 'y': -19}
              'id ','\n',                         #id  B9EF7451B8ACA33C1D9362E2649F14DA_element_153
               'text', d.text)'''


    browser.switch_to.default_content()
except Exception as er:
    print(f'Iframe error{i}')
'''time.sleep(2)

try:
    test_el = browser.find_element(By.TAG_NAME, 'div')

    print(f'текст в элементе div цикл{i}: ', test_el)
    main_button = browser.find_element(By.CSS_SELECTOR, 'a._main')
    main_button.click()
    print(f'main_button clicked цикл{i}')
except Exception as play_error:
    print(f' не нажалась play_error цикл{i}')

try:
    main_button=browser.find_element(By.CSS_SELECTOR, 'a._main')
    main_button.click()
except Exception as er:
    print(f'не нажалась a._main er цикл {i}')

try:
    button = WebDriverWait(browser, 5).until_not(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/Land"]')))
except Exception as er:
    print(f'не нажалась land err цикл{i}')

print(info, type(info))'''
