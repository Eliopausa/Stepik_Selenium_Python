import math
import time
from selenium import webdriver

link = "http://suninjuly.github.io/execute_script.html"

#  def calc(elem_x):
#      return str(math.log(abs(12*sin(elem_x))))

with webdriver.Chrome() as browser:
    browser.get(link)
    elem_button = browser.find_element_by_css_selector("button.btn.btn-primary")
    elem_x = browser.find_element_by_css_selector("span#input_value.nowrap").text
    anchor_elem_x = browser.find_element_by_css_selector("span#input_value.nowrap")
    browser.execute_script("return arguments[0].scrollIntoView(true);", anchor_elem_x)
    elem_x_summ = str(math.log(abs(12*math.sin(int(elem_x)))))
    input_1 = browser.find_element_by_css_selector("input#answer.form-control").send_keys(elem_x_summ)
    elem_checkbox = browser.find_element_by_css_selector("input#robotCheckbox").click()
    elem_radiobutton = browser.find_element_by_css_selector("input#robotsRule").click()
    elem_button.click()
    time.sleep(5)
