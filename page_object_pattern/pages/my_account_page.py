import logging
import allure

from selenium.webdriver.common.by import By

from page_object_pattern.pages.base_page import BasePage
from page_object_pattern.locators.locators import MyAccountPage as Locators


class MyAccountPage(BasePage):

    USERNAME_INPUT = Locators.username_input
    PASSWORD_INPUT = Locators.password_input
    REG_EMAIL_INPUT = Locators.reg_email_input
    REG_PASSWORD_INPUT = Locators.reg_password_input
    MY_ACCOUNT_LINK = Locators.my_account_link
    ERROR_MESSAGE = Locators.error_msg
    LOGOUT_LINK = Locators.logout_link
    LOGIN_BUTTON = (By.NAME, "login")
    REGISTER_BUTTON = (By.NAME, "register")

    def __init__(self, driver):
        super().__init__(driver)
        self.logger = logging.getLogger(__name__)

    @allure.step("Open My Account page")
    def open_page(self):
        self.driver.get("http://seleniumdemo.com/?page_id=7")

    @allure.step("Wait until My Account page is loaded")
    def wait_until_loaded(self):
        self.wait_for_visible(*self.REG_EMAIL_INPUT)

    @allure.step("Login user")
    def log_in(self, username, password):
        self.logger.info(f"Logging user: {username}")
        self.type(*self.USERNAME_INPUT, username)
        self.type(*self.PASSWORD_INPUT, password)
        self.click(*self.LOGIN_BUTTON)

    @allure.step("Logout user")
    def logout(self):
        self.logger.info("Logging out user")
        self.click(*self.LOGOUT_LINK)

    @allure.step("Create new account")
    def create_account(self, email, password):
        self.logger.info(f"Creating account: {email}")
        self.type(*self.REG_EMAIL_INPUT, email)
        self.type(*self.REG_PASSWORD_INPUT, password)
        self.click(*self.REGISTER_BUTTON)

    @allure.step("Check if logout link is displayed")
    def is_logout_link_displayed(self):
        return self.wait_for_visible(*self.LOGOUT_LINK).is_displayed()

    @allure.step("Get registration/login error message")
    def get_error_message(self):
        return self.get_text(*self.ERROR_MESSAGE)