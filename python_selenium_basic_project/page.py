from wrappers import WrappersClass
from selenium.webdriver.common.by import By
import time


class LoginPage(WrappersClass):

    def __init__(self, driver):
        super().__init__(driver)

    # Locators
    username_field = "username2"
    password_field = "password2"
    submit_button = "submit"
    page_title = "title"

    # Business flows
    def valid_login(self):
        self.enter_text(By.NAME, self.username_field, self.import_config("username"))
        self.enter_text(By.NAME, self.password_field, self.import_config("password"))
        self.click_element(By.ID, self.submit_button)
        time.sleep(5)

    def get_page_title(self):
        return self.get_element_text(By.ID, self.page_title)







