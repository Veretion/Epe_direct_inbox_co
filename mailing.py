
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import time, sleep, strftime
from random import randint
import pyautogui
import numpy as np
import settings_and_variables as sav

# variables

username = sav.username
password = sav.password
webpage  = sav.webpage
web_msg  = sav.web_msg

window_check1 = sav.window_check1
window_close1 = sav.window_close1
send_message1 = sav.send_message1
send_message2 = sav.send_message2


driver = webdriver.Chrome()
driver.implicitly_wait(5)

driver.get(webpage)  # переход по ссылке
sleep(randint(5, 8))

# находим поле для ввода логина и пароля
username_input = driver.find_element_by_css_selector("input[name='username']")
password_input = driver.find_element_by_css_selector("input[name='password']")

# вводим логин и пароль
username_input.clear()
username_input.send_keys(username)
sleep(randint(3, 5))
password_input.clear()
password_input.send_keys(password)


# жмём кнопку входа
password_input.send_keys(Keys.ENTER)
sleep(randint(8, 14))

# попытка перехода по ссылке сообщений или обновление
try:
    driver.get(webpage + web_msg)
except Exception as e:
    driver.refresh()
    print(e)
sleep(randint(4, 6))

# закрываем всплывающее окно (данные для входа)
if driver.find_element_by_xpath(window_check1):
    driver.find_element_by_xpath(window_close1).click()
else:
    pass
sleep(randint(8, 14))


text = open("logr.txt").read()

massiv = text.split('\n')
for i in massiv:
    try:
        sleep(randint(14, 33))
        # находим кнопку "отправить сообщение"
        if driver.find_element_by_xpath(send_message1):
            driver.find_element_by_xpath(send_message1).click()
        elif driver.find_element_by_xpath(send_message2):
            driver.find_element_by_xpath(send_message2).click()
        sleep(2)

        # вставляем имя пользователя в input
        log_input = driver.find_element_by_css_selector("input[name='queryBox']").send_keys(i)
        sleep(7)


        # кликаем по первому пользователю в списке
        try:
            driver.find_element_by_xpath(user_1)
            driver.find_element_by_xpath(user_2)
        except Exception as e:
            print(e)
            driver.find_elements_by_xpath(user_x)
        driver.find_elements_by_xpath(user_d)

        sleep(0.1)
        try:
            driver.find_element_by_xpath(ochnepeb_1).click()
        except:
            driver.find_elements_by_xpath(ochnepeb_2).click()
        sleep(5)

        # находим и нажимаем кнопку "далее"
        driver.find_element_by_xpath(BFS)
        sleep(1)
        driver.find_element_by_xpath(BFP).click()
        sleep(6)

        text_message_area = driver.find_element_by_xpath(send_message_area)
        text_message_area.clear()
        text_message_area.send_keys(message)
        sleep(randint(2, 4))
        text_message_area.send_keys(Keys.ENTER)
        print(i, "  сообщение отправлено ", str(strftime("%H:%M")))
        print("xx")

    except:
        print(i)
        driver.refresh()
        sleep(5)
        continue
