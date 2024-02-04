#https://habr.com/ru/articles/709314/
import time
from pprint import pprint

from selenium import webdriver
from selenium.common import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By
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

def go_home(browser): #возвращаемся домой (на страницу main) с любой страницы
        try:
            main_button = browser.find_element(By.CSS_SELECTOR, 'a[href="/Land"]')
            main_button.click()
        except Exception as err:
            print('def go_home err: ', err)
        time.sleep(1)
        print('Пришли домой')

def take_money(browser):  #собираем дань с владений
    global count
    try:
        land_butt=browser.find_element(By.CSS_SELECTOR, 'a[href="/Land/My"')
        if land_butt.text.strip() == 'Владения':   #проверяем готова ли дань
                                                   # (она готова когда текст == Владения)
            land_butt.click()
            # собираем дань
            take_button = browser.find_element(By.CSS_SELECTOR, 'a._marble')
            take_button.click()
            count+=1
            print('3 Собрали дань: ', count, ' раз.')
        else:
            print('4 It is not land time')
    except Exception as err:
        print('def take_money err: ', err)
    time.sleep(1)
    print('Собрали дань')

def do_patrol(browser):      #дозор проводим
    try:
        patrol_button = browser.find_element(By.XPATH, '//span[contains(text(), "Дозор")]')
        print(patrol_button.text)
        if patrol_button.text.strip() == 'Дозор':
            print('Patrol time!')
            patrol_button.click()
            for i in range(10):
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
        time.sleep(1)
    except Exception as err:
        print('def do_patrol err: ', err)
    print('Сходили в дозор')

def do_taverna_meet(browser):  #встречи в таверне
    global visit_count
    global not_accept_visit_count
    #допустимые посетители - с иконкой солдата, пустого разговора, золота
    good_visitors_image_url = ["https://lordy.mobi/images/icons/army.png", "https://lords.mobi/images/tavern/icon_talk.png", "https://lordy.mobi/images/tavern/icon_talk.png", "https://lordy.mobi/images/icons/gold.png"]
    #недопустимые - просят рубины
    bad_visitors_image_url = ["https://lordy.mobi/images/icons/ruby.png"]
    try:
        butt=browser.find_element(By.CSS_SELECTOR, 'a[href="/Tavern"')
        butt.click()
        visitors = browser.find_element(By.CSS_SELECTOR, '.btn_o_inner img')
        visitors_attribute = visitors.get_attribute('src')
        print('visitor_attribute: ', visitors_attribute)
        if visitors_attribute not in bad_visitors_image_url:  #если посетитель не просит рубинов
            visitors.click()
            print('not bad')
            #проверяем всплывающую кнопку
            active_butt = browser.find_element(By.CLASS_NAME, '_active')
            if active_butt:
                print('Всплывающая кнопка')
                active_butt.click()
                visit_count += 1
            else:
                print('Нет всплывающей кнопки')
            print('Accept visitors: ', visitors_attribute, 'accept visit_count: ', visit_count)
        else:
            #butt= browser.find_element(By.XPATH, '//span[contains(text(), "Пропустить")]')
            butt = browser.find_element(By.CSS_SELECTOR, 'a[href="/Tavern/Visitor_Skip"]')
            butt.click()
            not_accept_visit_count+=1
            print('Not accept visitors: ', visitors_attribute, 'count: ', not_accept_visit_count)
            active_butt = browser.find_element(By.CLASS_NAME, '_active')
            if active_butt:
                print('Всплывающая кнопка')
                active_butt.click()
                visit_count += 1
            else:
                print('Нет всплывающей кнопки')

    except Exception as err:
        print('do_taverna_meet err: ', err)
    time.sleep(1)
    print('Сходили в таверну')

def check_army(browser): #проверяем сколько солдат в наличии
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

def fight_glass_rat_raid(browser):
    try:
        raid_butt=browser.find_element(By.CSS_SELECTOR, 'a[href="/SingleRaids"')
        raid_butt.click()
        raid_butt = browser.find_element(By.CSS_SELECTOR, 'a[href="/SingleRaid/NewYear2024"')
        raid_butt.click()
        butt = browser.find_element(By.CSS_SELECTOR, 'div#lvl-37')
        butt.click()
        rat_health = browser.find_element(By.CSS_SELECTOR, '.combat-stats .text-left').text.strip()[:-1]
        print(rat_health)
        while rat_health:
            attack_butt = browser.find_element(By.CSS_SELECTOR, 'a[href="/SingleRaids/Hit"')
            attack_butt.click()
            rat_health = browser.find_element(By.CSS_SELECTOR, '.combat-stats .text-left').text.strip()[:-1]
            print(rat_health)
        continue_butt = browser.find_element(By.XPATH, '//span[contains(text(), "Продолжить рейд")]')
        continue_butt.click()
    except Exception as err:
        print('fight glass rat raid err: ', err)
    time.sleep(5)
    print('Сразились в рейде с ледяными крысами')


count_total = 0
while True:
    take_money(browser)
    go_home(browser)
    do_patrol(browser)
    go_home(browser)
    do_taverna_meet(browser)
    go_home(browser)
    print('ждем 1 сек')
    time.sleep(1)
    '''time.sleep(1)
    if check_army():
        fight_glass_rat_raid()
    else:
        print('No soldiers for fight')'''
    count_total+=1
    print('Количество пройденных циклов', count_total)



'''    # def take_money
    try:
        #владения, собираем дань
        land_butt=browser.find_element(By.CSS_SELECTOR, 'a[href="/Land/My"')
        print('1 butt_text: ', land_butt.text, ' current url: ', browser.current_url)
        current_url = browser.current_url
        if land_butt.text.strip() == 'Владения':
            print('2 land time!')
            land_butt.click()
            # собираем дань
            take_button = browser.find_element(By.CSS_SELECTOR, 'a._marble')
            take_button.click()
            count+=1
            print('3 Собрали дань: ', count, ' раз.')
            #land_point = 2
            current_url = browser.current_url
        else:
            print('4 It is not land time')
    except Exception as err:
        print(err)

    #if land_point == 2:  # 2 -lord is in the land
    #def go_home
    if current_url != 'https://lordy.mobi/Land': #если текущий юрл - не главная
                                                    # то переходим на главную
        try:
            # кликаем на главную
            main_button = browser.find_element(By.CSS_SELECTOR, 'a[href="/Land"]')
            main_button.click()
            print('5', main_button.text)
            time.sleep(5)
            current_url= browser.current_url
        except Exception as err:
            print(err)
    else:
        print(' 6 pass')
    print('7 Всего собрали дань: ', count, ' раз.')
    time.sleep(10)
    
    #def do_patrol
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
'''