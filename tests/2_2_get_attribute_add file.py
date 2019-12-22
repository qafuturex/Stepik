# -*- coding: utf-8 -*-

from selenium import webdriver
import time
import math
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(10)
    first_name = browser.find_element_by_css_selector('[name="firstname"]')
    first_name.click()
    first_name.send_keys('1name')
    last_name = browser.find_element_by_css_selector('[name="lastname"]')
    last_name.click()
    last_name.send_keys('2name')
    email = browser.find_element_by_css_selector('[name="email"]')
    email.click()
    email.send_keys('email')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'virus.txt')
    print(os.path.abspath(__file__))
    print(file_path)
    file = browser.find_element_by_css_selector('#file')
#   отсылаем файл, без клика
    file.send_keys(file_path)
    sbmt = browser.find_element_by_css_selector('.btn').click()

finally:
    time.sleep(5)
    browser.quit()
    #https://stepik.org/lesson/228249/step/8?unit=200781
