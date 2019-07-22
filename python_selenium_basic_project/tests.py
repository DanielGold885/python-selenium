import unittest
from selenium import webdriver
from page import LoginPage
import HtmlTestRunner


class TestClass(unittest.TestCase):

    driver = webdriver.Chrome()
    login_page = LoginPage(driver)

    @classmethod
    def setUpClass(cls):
        cls.driver.maximize_window()
        cls.driver.get(LoginPage.import_config("URL"))
        cls.driver.implicitly_wait(5)

    def test_method_valid_login(self):
        self.login_page.valid_login()
        self.assertEqual(LoginPage.import_config("title"), self.login_page.get_page_title())

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="./reports"), verbosity=2)
