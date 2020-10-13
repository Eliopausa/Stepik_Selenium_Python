import pytest
import math
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('link', [
    "236895",
    "236896",
    "236897",
    "236898",
    "236899",
    "236903",
    "236904",
    "236905"
    ]
                         )
class TestPages:
    def test_got_txt(self, browser, link):
        tmp_link = f"https://stepik.org/lesson/{link}/step/1"
        browser.get(tmp_link)
        WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "textarea")))
        answer = math.log(int(time.time()))
        browser.find_element_by_css_selector("textarea").send_keys(str(answer))
        button = browser.find_element_by_css_selector("button.submit-submission")
        button.click()
        WebDriverWait(browser, 5).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "pre.smart-hints__hint")))
        feedback = browser.find_element_by_css_selector("pre.smart-hints__hint").text
        assert str(feedback) == str("Correct!"), str(feedback)
