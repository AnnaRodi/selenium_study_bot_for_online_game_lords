#https://habr.com/ru/articles/709314/
import time
from pprint import pprint

from selenium import webdriver
from selenium.common import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import cookies

browser = webdriver.Chrome()
browser.implicitly_wait(5)
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
visit_count = 0
not_accept_visit_count = 0
#land_point = 1  #  1 - in main, 2 - in land
current_url = browser.current_url

def check_army(): #проверяем сколько солдат в наличии
    soldiers = None
    try:
        lord_resource = browser.find_element(By.CSS_SELECTOR, 'span.resource:nth-child(1) span')
        soldiers = lord_resource.text.strip()
        print('soldiers: ', soldiers)
        if int(soldiers)>5:
            return True
        else:
            return False
    except Exception as err:
        print('check_army err: ', err)
    print('Проверили количество солдат. Количество = ', soldiers)

fight_status = 0 # 0 начало, 1 ведется бой, 2 жмем кнопку продолжить
def fight_glass_rat_raid():
    global fight_status
    print('fight_status: ', fight_status)
    try:
        if not fight_status:
            raid_butt=browser.find_element(By.CSS_SELECTOR, 'a[href="/SingleRaids"')
            raid_butt.click()
            fight_status = 1
        else:
            try:
                continue_butt = browser.find_element(By.CSS_SELECTOR, 'div.main-button-inner')  #CONTINUE BUTTON
                continue_butt.click()
                fight_status = 1
            except Exception as er:
                print('try press continue button: ', er)
            rat_health = browser.find_element(By.CSS_SELECTOR, '.combat-stats .text-left').text.strip()[:-1]
            print(rat_health)
            while rat_health:
                #attack_butt = browser.find_element(By.CSS_SELECTOR, 'a[href="/SingleRaids/Hit"')
                attack_butt = browser.find_element(By.CSS_SELECTOR, 'a.btn-attack')#attack_butt = WebDriverWait(browser, 5).until_not(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/SingleRaids/Hit"')))
                attack_butt.click()
                new_rat_health = browser.find_element(By.CSS_SELECTOR, '.combat-stats .text-left').text.strip()[:-1]
                rat_health= new_rat_health
                print(rat_health)


    except Exception as err:
        print('fight glass rat raid err: ', err)
    time.sleep(5)
    print('Сразились в рейде с ледяными крысами')


count_total = 0
while True:
    """take_money()
    go_home()
    do_patrol()
    go_home()
    do_taverna_meet()
    go_home()
    time.sleep(1)"""
    fight_glass_rat_raid()
    '''if check_army():
        fight_glass_rat_raid()
    else:
        print('No soldiers for fight')'''
    count_total+=1
    print('Количество пройденных циклов', count_total)
