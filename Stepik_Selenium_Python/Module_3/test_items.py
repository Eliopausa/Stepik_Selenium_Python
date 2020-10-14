import pytest
import math
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import FirefoxProfile


def test_items(browser):
    try:
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(link)
        elem_btn = browser.find_element_by_css_selector("button.btn-lg.btn-primary.btn-add-to-basket")
    except:
        elem_btn = None
    assert elem_btn is not None, 'Could not find element - "Add to basket" button'

