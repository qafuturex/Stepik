from selenium import webdriver
import time, unittest
from selenium.webdriver.support.ui import Select

try:
    link = "http://suninjuly.github.io/selects1.html"
    wd = webdriver.Chrome()
    wd.get(link)

    def calc(x, z):
        return str(int(x)+int(z))

    x_element = wd.find_element_by_id('num1')
    x1 = x_element.text
    z_element = wd.find_element_by_id('num2')
    z1 = z_element.text
    y = calc(x1, z1)
    print(y)
    DropDown = Select(wd.find_element_by_tag_name("select"))
    DropDown.select_by_value(y)
    Submit = wd.find_element_by_css_selector('[type="submit"]').click()
finally:
    time.sleep(10)
    wd.quit()





