from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration1.html"

with webdriver.Chrome() as browser:
    browser.get(link)
    elements = browser.find_elements_by_css_selector("input[type='text']")
    for element in elements:
        element.send_keys("answer")
    button = browser.find_element_by_xpath("//button[@type=\"submit\"]")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text