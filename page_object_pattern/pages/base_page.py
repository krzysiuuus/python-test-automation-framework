import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def click(self, by, locator):
        self.wait.until(ec.element_to_be_clickable((by, locator))).click()

    def type(self, by, locator, text, clear_first=True):
        element = self.wait.until(ec.visibility_of_element_located((by, locator)))
        if clear_first:
            element.clear()
        element.send_keys(text)

    def get_text(self, by, locator):
        return self.wait.until(ec.visibility_of_element_located((by, locator))).text

    def find(self, by, locator):
        return self.wait.until(ec.visibility_of_element_located((by, locator)))

    def finds(self, by, locator):
        return self.wait.until(ec.presence_of_all_elements_located((by, locator)))

    def wait_for_visible(self, by, locator):
        return self.wait.until(ec.visibility_of_element_located((by, locator)))

    def wait_for_clickable(self, by, locator):
        return self.wait.until(ec.element_to_be_clickable((by, locator)))

    def wait_for_all_visible(self, by, locator):
        return self.wait.until(ec.visibility_of_all_elements_located((by, locator)))

    def is_visible(self, by, locator):
        try:
            self.wait.until(ec.visibility_of_element_located((by, locator)))
            return True
        except Exception:
            return False

    def attach_screenshot(self, name="screenshot"):
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name=name,
            attachment_type=AttachmentType.PNG
        )