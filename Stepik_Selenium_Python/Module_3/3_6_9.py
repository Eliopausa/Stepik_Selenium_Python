import pytest
import math
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import FirefoxProfile
from selenium.common.exceptions import NoSuchElementException


def test_items(browser):
    try:
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(link)
        elem_btn = browser.find_element_by_css_selector("button.btn-lg.btn-primary.btn-add-to-basket")
    except:
        elem_btn = None
    assert elem_btn is not None, "test text"

# pytest "C:\Users\D.ryzhenkov.HORATIO\Projects\Stepik_Selenium_Python\Module_3\Test_tab.py" --browser_name=chrome -v --language=en