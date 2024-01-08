#https://habr.com/ru/articles/709314/
import time
from pprint import pprint

from selenium import webdriver
from selenium.common import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from config import cookies

browser = webdriver.Chrome()

#открываем сайт, логинимся и переходим в игру
try:
    browser.get("https://vmmo.mobi/menu")

    browser.implicitly_wait(5)
    play_button = browser.find_element(By.CSS_SELECTOR, 'li:nth-child(1) .va-m')
    print('play_button текст: ', play_button.text)
    log_in_button = browser.find_element(By.CSS_SELECTOR, 'li:nth-child(2) .va-m')
    print('log_in_button текст: ', log_in_button.text)
    log_in_button.click()
    #перешли на вкладку регистрация
    login_tab = browser.find_element(By.CSS_SELECTOR, 'span.tab')
    print('reg_tab text: ', login_tab.text)
    login_tab.click()
    #заполняем логин пароль
    login_input = browser.find_element(By.CSS_SELECTOR, 'input#login')
    login_input.send_keys(cookies['login'])
    password_input = browser.find_element(By.CSS_SELECTOR, 'input#password')
    password_input.send_keys(cookies['password'])
    #жмем кнопку войти
    reg_button = browser.find_element(By.CSS_SELECTOR, 'button.btn-green')
    print(reg_button.text)
    reg_button.click()
    #выбираем игру могущество лордов
    game_lords = browser.find_element(By.CSS_SELECTOR, 'div.b-list-games:nth-child(5)')
    game_lords.click()
except NoSuchElementException as entry_error:
    print(entry_error)

count = 0
land_point = 1  #  1 - in main, 2 - in land
while True:
    try:
        #владения, собираем дань
        land_butt=browser.find_element(By.CSS_SELECTOR, 'a[href="/Land/My"')
        print('1 text: ', land_butt.text)
        if land_butt.text.strip() == 'Владения':
            print('2 land time!')
            land_butt.click()
            # собираем дань
            take_button = browser.find_element(By.CSS_SELECTOR, 'a._marble')
            take_button.click()
            count+=1
            print('3 Собрали дань: ', count, ' раз.')
            land_point = 2
        else:
            print('4 It is not land time')
    except Exception as err:
        print(err)

    if land_point == 2:  # 2 -lord is in the land
        try:
            # кликаем на главную
            main_button = browser.find_element(By.CSS_SELECTOR, 'a[href="/Land"]')
            main_button.click()
            print('5', main_button.text)
            time.sleep(5)
        except Exception as err:
            print(err)
    else:
        print(' 6 pass')
    print('7 Всего собрали дань: ', count, ' раз.')
    time.sleep(10)
    '''
        #дозор, проводим
        patrol_button = browser.find_element(By.XPATH, '//span[contains(text(), "Дозор")]')
        print(patrol_button.text)
        if patrol_button.text.strip() == 'Дозор':
            print('Patrol time!')
            patrol_button.click()
            for i in range(5):
                # собираем дань
                take_button = browser.find_element(By.CSS_SELECTOR, 'div.main-button-inner')
                take_button.click()
                print('проводим дозор '+ str(i))
            # кликаем на главную
            main_button = browser.find_element(By.CSS_SELECTOR, 'a[href="/Land"]')
            main_button.click()
            print(main_button.text)
        else:
            print('It is not patrol time')
        time.sleep(5)
    '''



    '''#играем
    while True:
        #кликаем на главную
        main_button = browser.find_element(By.CSS_SELECTOR, 'a[href="/Land"]')
        main_button.click()
        print(main_button.text)
        try:
            #кликаем владения
            land_button = browser.find_element(By.XPATH, '//span[text()="Владения"]')
            land_button.click()
            print('land_button.text', land_button)
            print('кликнули владения')
        except NoSuchElementException as land_err:
            print(land_err)
        except StaleElementReferenceException as old_err:
            print(old_err)
    
        try:
            #собираем дань
            take_button = browser.find_element(By.CSS_SELECTOR, 'a._marble')
            take_button.click()
            print('Собрали дань')
        except NoSuchElementException as button_error:
            print('button_error: дань с владений не готова', button_error)
    
    
        #кликаем на главную
        main_button = browser.find_element(By.CSS_SELECTOR, 'a[href="/Land"]')
        main_button.click()
        print(main_button.text)'''


