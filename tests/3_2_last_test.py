
from selenium import webdriver
import time
import unittest

class TestForm(unittest.TestCase):

    def test1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        firstName = browser.find_element_by_css_selector('.first_block > .form-group.first_class :nth-child(2)')
        firstName.send_keys('Олег')
        LastName = browser.find_element_by_xpath('/html/body/div/form/div[1]/div[2]/input')
        LastName.send_keys('Тинькофф')
        Email = browser.find_element_by_xpath('/html/body/div/form/div[1]/div[3]/input')
        Email.send_keys('olegka@mail.ru')
        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
        browser.quit()

    def test2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        firstName = browser.find_element_by_css_selector('.first_block > .form-group.first_class :nth-child(2)')
        firstName.send_keys('Олег')
        LastName = browser.find_element_by_xpath('/html/body/div/form/div[1]/div[2]/input')
        LastName.send_keys('Тинькофф')
        Email = browser.find_element_by_xpath('/html/body/div/form/div[1]/div[3]/input')
        Email.send_keys('olegka@mail.ru')
        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
        browser.quit()

if __name__ == "__main__":
    unittest.main()

#ссылка на задание https://stepik.org/lesson/36285/step/13?unit=162401