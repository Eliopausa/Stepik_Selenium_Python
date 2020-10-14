import pytest
import math
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


link = "http://selenium1py.pythonanywhere.com/"

def test_guest_should_see_login_link_pass(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")

def test_guest_should_see_login_link_fail(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#magic_link")

    # usage pytest "C:\Users\D.ryzhenkov.HORATIO\Projects\Stepik_Selenium_Python\Module_3\3_2_testtab.py" --browser_name=firefox -v
    #  --tb=line --reruns 1