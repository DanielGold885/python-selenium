from base import BaseClass
import traceback


class WrappersClass(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)

    def enter_text(self, By, element, value):
        try:
            element = self.driver.find_element(By, element)
            element.clear()
            element.send_keys(value)
            print("enter_text - Was Successful")
        except:
            print("update_text_field - Failed")
            self.driver.save_screenshot("C:\\seleniumDrivers\\reports")
            self.fail("enter_text - Failed" + str(element) + str(traceback.format_exc()))

    def click_element(self, By, element):
        try:
            element = self.driver.find_element(By, element)
            element.click()
            print("Click was successful!")
        except:
            print("Could not click on Element!")
            self.driver.save_screenshot("C:\\seleniumDrivers\\reports")
            self.fail("The click failed" + str(element) + str(traceback.format_exc()))

    def get_element_text(self, By, element):
        try:
            element = self.driver.find_element(By, element)
            return element.text
        except:
            print("Could not get text")
            self.driver.save_screenshot("C:\\seleniumDrivers\\reports")
            self.fail("Could not get text" + str(element) + str(traceback.format_exc()))


