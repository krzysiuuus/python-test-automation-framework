from selenium.webdriver.common.keys import Keys

import page_object_pattern.locators.locators


class MyAccountPage:

    def __init__(self, driver):
        self.driver = driver
        # my account page elements
        self.username_input = page_object_pattern.locators.locators.MyAccountPage.username_input
        self.password_input = page_object_pattern.locators.locators.MyAccountPage.password_input
        self.reg_email_input = page_object_pattern.locators.locators.MyAccountPage.reg_email_input
        self.reg_password_input = page_object_pattern.locators.locators.MyAccountPage.reg_password_input
        self.my_account_link = page_object_pattern.locators.locators.MyAccountPage.my_account_link
        self.error_msg = page_object_pattern.locators.locators.MyAccountPage.error_msg
        self.logout_link= page_object_pattern.locators.locators.MyAccountPage.logout_link

    def open_page(self):
        self.driver.get("http://seleniumdemo.com/?page_id=7")

    def log_in(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.password_input).send_keys(Keys.ENTER)

    def logout(self):
        self.driver.find_element(*self.logout_link).click()

    def create_account(self, email, password):
        self.driver.find_element(*self.reg_email_input).send_keys(email)
        self.driver.find_element(*self.reg_password_input).send_keys(password)
        self.driver.find_element(*self.reg_password_input).send_keys(Keys.ENTER)

    def is_logout_link_displayed(self):
        return self.driver.find_element(*self.logout_link).is_displayed()

    def get_error_message(self):
        return self.driver.find_element(*self.error_msg).text