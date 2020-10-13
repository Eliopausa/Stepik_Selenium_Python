import math
import time
from selenium import webdriver

#  Ебантология отсюда - https://stepik.org/lesson/165493/step/5?unit=140087
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"

with webdriver.Chrome() as browser:
    browser.get(link)
    x_element = browser.find_element_by_id("input_value")
    x=x_element.text
    y=calc(x)
    input1 = browser.find_element_by_css_selector("input#answer.form-control")
    input1.send_keys(y)
    checkbox1 = browser.find_element_by_css_selector("label.form-check-label")
    checkbox1.click()
    radiobutton1 = browser.find_element_by_id("robotsRule")
    radiobutton1.click()
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(5)




