import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

links = [
    ("https://stepik.org/lesson/236895/step/1"),
    ("https://stepik.org/lesson/236896/step/1"),
    ("https://stepik.org/lesson/236897/step/1"),
    ("https://stepik.org/lesson/236898/step/1"),
    ("https://stepik.org/lesson/236899/step/1"),
    ("https://stepik.org/lesson/236903/step/1"),
    ("https://stepik.org/lesson/236904/step/1"),
    ("https://stepik.org/lesson/236905/step/1")
]

@pytest.fixture(scope="function")
def browser():
    print("\nstart dr for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit dr..")
    browser.quit()

@pytest.mark.parametrize('link', links)
def test_check_down(browser, link):
    answer = math.log(int(time.time()))
    browser.get(link)
    area_presence = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".textarea.string-quiz__textarea")))
    area = browser.find_element(By.CSS_SELECTOR, ".textarea.string-quiz__textarea")
    area.send_keys(str(answer))
    #WebDriverWait(browser, 30).until(
    #    EC.presence_of_element_located((By.CSS_SELECTOR, ".submit-submission")))
    submit = browser.find_element_by_css_selector(".submit-submission")
    submit.click()
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint")))
    correct = browser.find_element_by_css_selector(".smart-hints__hint").text
    assert correct == "Correct!", correct




