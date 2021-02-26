
import time
import datetime


file = open("mailing.py", 'r', encoding='utf-8').read()

x = file.split('кликаем')[1]

print(x.split('find_element_by_xpath')[0])

