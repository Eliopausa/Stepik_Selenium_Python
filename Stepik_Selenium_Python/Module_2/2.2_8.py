import time
import os
import pyperclip
from selenium import webdriver

link = "http://suninjuly.github.io/file_input.html"

with webdriver.Chrome() as browser:
    browser.get(link)
    first_name = browser.find_element_by_css_selector("input[name='firstname']").send_keys("firstname")
    last_name = browser.find_element_by_css_selector("input[name='lastname']").send_keys("lastname")
    email_name = browser.find_element_by_css_selector("input[name='email']").send_keys("email@mail.com")
    elem_attach = browser.find_element_by_css_selector("input#file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, "testfile.txt")
    elem_attach.send_keys(file_path)
    submit_button = browser.find_element_by_css_selector("button.btn").click()
    alert = browser.switch_to.alert
    alert_text = alert.text
    addToClipBoard = alert_text.split(': ')[-1]
    pyperclip.copy(addToClipBoard)
    time.sleep(10)
