from selenium import webdriver
import time

link = "http://suninjuly.github.io/huge_form.html"

with webdriver.Chrome() as browser:
    browser.get(link)
    elements = browser.find_elements_by_css_selector("input[type='text']")
    for element in elements:
        element.send_keys("answer")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(10)


