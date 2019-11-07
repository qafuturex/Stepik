# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    browser.get(link)
#ждём, пока появится заданный текст
    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
#кликаем кнопку
    button = browser.find_element_by_css_selector('#book')
    button.click()
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

# ищем значение переменной, считаем ответ
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
# ищем поле ввода ответа, втыкаем ответ
    insrt = browser.find_element_by_id('answer')
    insrt.click()
    insrt.send_keys(y)
    btn = browser.find_element_by_css_selector('#solve')
    btn.click()
finally:
    time.sleep(5)
    browser.quit()

#https://stepik.org/lesson/181384/step/8?unit=156009
# задание 2.4, ожидание