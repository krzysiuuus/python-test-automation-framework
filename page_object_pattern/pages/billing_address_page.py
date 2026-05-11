import logging
import allure
from selenium.webdriver.support.select import Select

from page_object_pattern.pages.base_page import BasePage
from page_object_pattern.locators.locators import BillingAddressLocators


class BillingAddressPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.logger = logging.getLogger(__name__)

        self.first_name_input = BillingAddressLocators.first_name_input
        self.last_name_input = BillingAddressLocators.last_name_input
        self.addresses_link = BillingAddressLocators.addresses_link
        self.edit_link = BillingAddressLocators.edit_link
        self.country_select = BillingAddressLocators.country_select
        self.address_input = BillingAddressLocators.address_input
        self.postcode_input = BillingAddressLocators.postcode_input
        self.city_input = BillingAddressLocators.city_input
        self.phone_input = BillingAddressLocators.phone_input
        self.save_address_button = BillingAddressLocators.save_address_button
        self.message = BillingAddressLocators.message

    @allure.step("Open billing address edit form")
    def open_edit_billing_address(self):
        self.logger.info("Opening billing address edit form")
        self.driver.find_element(*self.addresses_link).click()
        self.driver.find_element(*self.edit_link).click()
        self.attach_screenshot("open_edit_billing_address")

    @allure.step("Set personal data")
    def set_personal_data(self, first_name, last_name):
        self.logger.info(f"Setting personal data: {first_name} {last_name}")
        self.type(*self.first_name_input, first_name)
        self.type(*self.last_name_input, last_name)
        self.attach_screenshot("set_personal_data")

    @allure.step("Select country")
    def select_country(self, country):
        self.logger.info(f"Selecting country: {country}")
        country_select = self.find(*self.country_select)
        Select(country_select).select_by_visible_text(country)
        self.attach_screenshot("select_country")

    @allure.step("Set address")
    def set_address(self, street, postcode, city):
        self.logger.info(
            f"Setting address: {street}, {postcode}, {city}"
        )
        self.type(*self.address_input, street)
        self.type(*self.postcode_input, postcode)
        self.type(*self.city_input, city, clear_first=False)
        self.attach_screenshot("set_address")

    @allure.step("Set phone number")
    def set_phone_number(self, number):
        self.logger.info(f"Setting phone number: {number}")
        self.type(*self.phone_input, number)
        self.attach_screenshot("set_phone_number")

    @allure.step("Save billing address")
    def save_address(self):
        self.logger.info("Saving billing address")
        self.click(*self.save_address_button)
        self.attach_screenshot("save_address")

    @allure.step("Get success message")
    def get_message_text(self):
        return self.get_text(*self.message)