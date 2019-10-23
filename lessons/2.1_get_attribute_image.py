

from selenium import webdriver
import time
import math
try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
#
    x_element = browser.find_element_by_id('treasure')
    x = x_element.get_attribute('valuex')
    print(x)
    y = calc(x)
#
    insrt = browser.find_element_by_id('answer')
    insrt.send_keys(y)
    time.sleep(1)


    chk = browser.find_element_by_id('robotCheckbox')
    chk.click()
    time.sleep(1)

    rd = browser.find_element_by_id('robotsRule')
    rd.click()
    time.sleep(1)
    btn = browser.find_element_by_css_selector('.btn')
    btn.click()
finally:
    time.sleep(5)
    browser.quit()

# https://stepik.org/lesson/165493/step/7?unit=140087 module 2
