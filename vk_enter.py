#https://habr.com/ru/articles/709314/
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

#открываем сайт, логинимся и переходим в игру
try:
    browser.get("https://vk.com/feed")
    time.sleep(30)
    browser.implicitly_wait(5)
    while True:
        play_button = browser.find_element(By.CSS_SELECTOR, 'div.land-menu')
        print('play_button текст: ', play_button.text)
        print('title: ', browser.title)
        print('url: ', browser.current_url)
except Exception as entry_error:
    print(entry_error)
