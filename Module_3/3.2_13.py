# import time
# import unittest
# import Registration_module
# import Class_TryUnitTest
# from selenium import webdriver
#
# # Для импорта пользовательских модулей из надо положить в sys path, в моем случае в PyCharm это C:\Projects\Scripts
# # Модуль Registration_module содержит функцию, которая принимает url, выполняет регистрацию
# # и возвращает текст приветствия
# # Модуль Class_TryUnitTest сверяет значение, которое возвращает Registration_module с контрольным
# # и в случае несоответствия возвращает текст ошибки
#
# url1 = "http://suninjuly.github.io/registration1.html"
# url2 = "http://suninjuly.github.io/registration2.html"
# Class_TryUnitTest.TryUnitTest().test_page(url1)
# Class_TryUnitTest.TryUnitTest().test_page(url2)


import time
import unittest
from selenium import webdriver


class TryUnitTest(unittest.TestCase):

    # Все это полная хуйня, хоть и работает. Регистрацию нужно упаковать в функцию, принимающую URL и возвращающую
    # "welcome_text" и вызывать ее для проверки результата в тестовом классе. В саму функцию так же добавить
    # исключение для случая не успешной регистрации. В возвращаемом тексте публиковать URL, гле регистрация не
    # прошла.
    # А сейчас все остается так как есть, потому что я нихуян е знаю на данный момент синтаксиса для написания
    # кода как следует.
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/registration1.html")
    input_your_first_name = browser.find_element_by_css_selector("input[class='form-control first'][required]")
    input_your_first_name.send_keys("answer")
    input_your_last_name = browser.find_element_by_css_selector("input[class='form-control second'][required]")
    input_your_last_name.send_keys("answer")
    input_email = browser.find_element_by_css_selector("input[class='form-control third'][required]")
    input_email.send_keys("answer")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(1)
    welcome_text: object = browser.find_element_by_tag_name("h1").text
    browser.close()

    def test_page1(self):
    self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "test_page test failed")

    def shutDown(self):
    self.driver.close()

    # browser.get("http://suninjuly.github.io/registration2.html")
    # input_your_first_name = browser.find_element_by_css_selector("input[class='form-control first'][required]")
    # input_your_first_name.send_keys("answer")
    # input_your_last_name = browser.find_element_by_css_selector("input[class='form-control second'][required]")
    # input_your_last_name.send_keys("answer")
    # input_email = browser.find_element_by_css_selector("input[class='form-control third'][required]")
    # input_email.send_keys("answer")
    # button = browser.find_element_by_css_selector("button.btn")
    # button.click()
    # time.sleep(1)
    # welcome_text = browser.find_element_by_tag_name("h1").text

    def test_page2(self):
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!",
                         "test_page test failed")

    def shutDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
