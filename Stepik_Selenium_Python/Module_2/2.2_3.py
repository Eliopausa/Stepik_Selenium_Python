import time
import math
from selenium import webdriver
from selenium.webdriver.support.ui import Select

# Ебантология отсюда - https://stepik.org/lesson/228249/step/3?unit=200781

link = "http://suninjuly.github.io/selects1.html"


with webdriver.Chrome() as browser:
    browser.get(link)
    elem1 = browser.find_element_by_id("num1").text
    elem2 = browser.find_element_by_id("num2").text
    summ1 = int(elem1) + int(elem2)
    select = Select(browser.find_element_by_css_selector("select"))
    # Значение переводится в строку из числа
    summ2 = str(summ1)
    select.select_by_value(summ2)
    button = browser.find_element_by_css_selector("button.btn").click()
    time.sleep(5)
    print(summ1)




