

from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_id('input_value')
x = x_element.text
y = calc(x)
insrt = browser.find_element_by_id('answer')
insrt.send_keys(y)
time.sleep(1)
chk = browser.find_element_by_id('robotCheckbox')
chk.click()
time.sleep(1)
rd = browser.find_element_by_css_selector('.form-radio-custom > input')
rd.click()
time.sleep(1)
btn = browser.find_element_by_css_selector('.btn')
btn.click()
time.sleep(5)
browser.quit()
#https://stepik.org/lesson/165493/step/5?unit=140087
