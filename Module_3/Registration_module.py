import time
from selenium import webdriver


def registration(url):
    browser = webdriver.Chrome()
    try:
        browser.get(url)
        input_your_first_name = browser.find_element_by_css_selector("input[class='form-control first'][required]")
        input_your_first_name.send_keys("answer")
        input_your_last_name = browser.find_element_by_css_selector("input[class='form-control second'][required]")
        input_your_last_name.send_keys("answer")
        input_email = browser.find_element_by_css_selector("input[class='form-control third'][required]")
        input_email.send_keys("answer")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_text: object = browser.find_element_by_tag_name("h1").text
        return welcome_text
    except Exception:
        browser.close()
