import math, time
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

with webdriver.Chrome() as browser:
    browser.implicitly_wait(10)
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    button_book = browser.find_element_by_css_selector(".btn")
    price_event = WebDriverWait(browser,10).until(EC.text_to_be_present_in_element((By.ID, "price"), str(100)))
    button_book.click()
    elem_x = browser.find_element_by_css_selector("#input_value").text
    elem_x_summ = str(math.log(abs(12 * math.sin(int(elem_x)))))
    input_1 = browser.find_element_by_css_selector("#answer").send_keys(elem_x_summ)
    submit_button = browser.find_element_by_css_selector("#solve").click()
    alert = browser.switch_to.alert
    alert_text = alert.text
    addToClipBoard = alert_text.split(': ')[-1]
    pyperclip.copy(addToClipBoard)
