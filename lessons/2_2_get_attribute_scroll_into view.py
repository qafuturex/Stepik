# -*- coding: utf-8 -*-

from selenium import webdriver
import time
import math
try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
# ищем значение переменной, считаем ответ
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
# ищем поле ввода ответа, втыкаем ответ
    insrt = browser.find_element_by_id('answer')
    insrt.send_keys(y)
# проверяем значение у пипл радио
    people_radio = browser.find_element_by_id("peopleRule")
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    assert people_checked is not None, "People radio is not selected by default"

# проверяем значение атрибута disabled у кнопки Submit
    button = browser.find_element_by_css_selector('.btn')
    button_disabled = button.get_attribute("disabled")
    print("value of button Submit: ", button_disabled)
    assert button_disabled is None

# ищем радиобаттон роботЫ
    chk = browser.find_element_by_id('robotCheckbox')
    chk.click()
# find radiobutton, scroll into view, click
    rd = browser.find_element_by_css_selector('.form-radio-custom > input')
    browser.execute_script("return arguments[0].scrollIntoView(true);", rd)
    rd.click()
# find submit, click
    btn = browser.find_element_by_css_selector('.btn')
    btn.click()
finally:
    time.sleep(5)
    browser.quit()
    #https://stepik.org/lesson/165493/step/5?unit=140087
