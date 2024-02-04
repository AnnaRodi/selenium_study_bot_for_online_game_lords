import time
from selenium.webdriver.common.by import By

count = 0

def go_home(browser):  # возвращаемся домой (на страницу main) с любой страницы
    try:
        main_button = browser.find_element(By.CSS_SELECTOR, 'a[href="/Land"]')
        main_button.click()
    except Exception as err:
        print('def go_home err: ', err)
    time.sleep(1)
    print('Пришли домой')


def take_money(browser):  # собираем дань с владений
    global count
    try:
        land_butt = browser.find_element(By.CSS_SELECTOR, 'a[href="/Land/My"')
        if land_butt.text.strip() == 'Владения':  # проверяем готова ли дань
            # (она готова когда текст == Владения)
            land_butt.click()
            # собираем дань
            take_button = browser.find_element(By.CSS_SELECTOR, 'a._marble')
            take_button.click()
            count += 1
            print('3 Собрали дань: ', count, ' раз.')
        else:
            print('4 It is not land time')
    except Exception as err:
        print('def take_money err: ', err)
    time.sleep(1)
    print('Собрали дань')


def do_patrol(browser):  # дозор проводим
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
                print('проводим дозор ' + str(i))
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


def do_taverna_meet(browser):  # встречи в таверне
    global visit_count
    global not_accept_visit_count
    # допустимые посетители - с иконкой солдата, пустого разговора, золота
    good_visitors_image_url = ["https://lordy.mobi/images/icons/army.png",
                               "https://lords.mobi/images/tavern/icon_talk.png",
                               "https://lordy.mobi/images/tavern/icon_talk.png",
                               "https://lordy.mobi/images/icons/gold.png"]
    # недопустимые - просят рубины
    bad_visitors_image_url = ["https://lordy.mobi/images/icons/ruby.png"]
    try:
        butt = browser.find_element(By.CSS_SELECTOR, 'a[href="/Tavern"')
        butt.click()
        visitors = browser.find_element(By.CSS_SELECTOR, '.btn_o_inner img')
        visitors_attribute = visitors.get_attribute('src')
        print('visitor_attribute: ', visitors_attribute)
        if visitors_attribute not in bad_visitors_image_url:  # если посетитель не просит рубинов
            visitors.click()
            print('not bad')
            # проверяем всплывающую кнопку
            active_butt = browser.find_element(By.CLASS_NAME, '_active')
            if active_butt:
                print('Всплывающая кнопка')
                active_butt.click()
                visit_count += 1
            else:
                print('Нет всплывающей кнопки')
            print('Accept visitors: ', visitors_attribute, 'accept visit_count: ', visit_count)
        else:
            # butt= browser.find_element(By.XPATH, '//span[contains(text(), "Пропустить")]')
            butt = browser.find_element(By.CSS_SELECTOR, 'a[href="/Tavern/Visitor_Skip"]')
            butt.click()
            not_accept_visit_count += 1
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


def check_army(browser):  # проверяем сколько солдат в наличии
    soldiers = None
    try:
        lord_resource = browser.find_element(By.CSS_SELECTOR, 'span.resource:nth-child(1) span')
        soldiers = lord_resource.text.strip()
        print('soldiers: ', soldiers)
        if int(soldiers) > 5:
            return True
        else:
            return False
    except Exception as err:
        print('check_army err: ', err)
    print('Проверили количество солдат. Количество = ', soldiers)


def fight_glass_rat_raid(browser):
    try:
        raid_butt = browser.find_element(By.CSS_SELECTOR, 'a[href="/SingleRaids"')
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