import time
import unittest
from selenium import webdriver
import Registration_module


class TryUnitTest(unittest.TestCase):

    def test_page_1(self, url1):
        url = url1
        self.assertEqual(Registration_module.registration(url),
                         "Congratulations! You have successfully registered!", "url test failed")

    def test_page_2(self, url2):
        url = url2
        self.assertEqual(Registration_module.registration(url),
                         "Congratulations! You have successfully registered!", "url test failed")

if __name__ == "__main__":
    unittest.main()
