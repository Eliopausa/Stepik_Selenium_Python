import time
import math
import pyperclip
from selenium import webdriver

with webdriver.Chrome() as browser:
    browser.get("http://suninjuly.github.io/alert_accept.html")
    btn_1 = browser.find_element_by_css_selector("button.btn.btn-primary").click()
    time.sleep(10)
    alert_1 = browser.switch_to.alert
    alert_1.accept()
    elem_x = browser.find_element_by_css_selector("#input_value").text
    elem_x_summ = str(math.log(abs(12 * math.sin(int(elem_x)))))
    input_1 = browser.find_element_by_css_selector("input#answer").send_keys(elem_x_summ)
    submit_button = browser.find_element_by_css_selector("button.btn").click()
    alert = browser.switch_to.alert
    alert_text = alert.text
    addToClipBoard = alert_text.split(': ')[-1]
    pyperclip.copy(addToClipBoard)


