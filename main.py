import time

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

#играем
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
    print(main_button.text)

    # деремся на главной
    time.sleep(5)
    for i in range(3):
        try:
            land_mob = browser.find_element(By.CSS_SELECTOR, 'a.land-mob-link')
            print(land_mob.text)
            land_mob.click()
            # процесс драки
            try:
                #считываем здоровье моба
                enemy_health = browser.find_element(By.CSS_SELECTOR, 'span#enemy-health')
                enemy_health= int(enemy_health.text)
                print('enemy_health', enemy_health)
                while enemy_health>0:
                    fight_button = browser.find_element(By.CSS_SELECTOR, 'a.combat-attack-link')
                    fight_button.click()
                    enemy_health = browser.find_element(By.CSS_SELECTOR, 'span#enemy-health')
                    enemy_health = int(enemy_health.text)
                    print('enemy_health', enemy_health)
            except NoSuchElementException:
                print('no enemy health')
            #забрали добычу
            take_btn = browser.find_element(By.CSS_SELECTOR, 'a[href="/BattleInvasion/victory"')
            take_btn.click()
        except NoSuchElementException:
            print("NoSuchElementException  land_mob = browser.find_element(By.CSS_SELECTOR, 'a.land-mob-link')")


time.sleep(15)
browser.quit()

