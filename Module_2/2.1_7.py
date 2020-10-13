import math
import time
from selenium import webdriver

#  Ебантология отсюда - https://stepik.org/lesson/165493/step/7?unit=140087
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

with webdriver.Chrome() as browser:
    browser.get(link)
    a_element = browser.find_element_by_id("treasure")
    x=a_element.get_attribute("valuex")
    y=calc(x)
    input1 = browser.find_element_by_css_selector("#answer").send_keys(y)
    checkbox1 = browser.find_element_by_id("robotCheckbox").click()
    radiobutton1 = browser.find_element_by_id("robotsRule").click()
    button = browser.find_element_by_css_selector("button.btn").click()
    time.sleep(5)