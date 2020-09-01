from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration2.html"

with webdriver.Chrome() as browser:
    browser.get(link)

    # Заполнение поля First name
    input_your_first_name = browser.find_element_by_css_selector("input[class='form-control first'][required]")
    input_your_first_name.send_keys("answer")

    # Заполнение поля Last name
    input_your_last_name = browser.find_element_by_css_selector("input[class='form-control second'][required]")
    input_your_last_name.send_keys("answer")

    # Заполнение поля Email
    input_email = browser.find_element_by_css_selector("input[class='form-control third'][required]")
    input_email.send_keys("answer")

    # Нажатие кнопки Submit
    button = browser.find_element_by_css_selector("button.btn")
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


