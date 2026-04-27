from selenium.webdriver.support.select import Select

import page_object_pattern.locators.locators

class BillingAddressPage:

    def __init__(self, driver):
        self.driver = driver
        #Billing Address Page elements
        self.first_name_input = locators.locators.BillingAddressLocators.first_name_input
        self.last_name_input = locators.locators.BillingAddressLocators.last_name_input
        self.addresses_link = locators.locators.BillingAddressLocators.addresses_link
        self.edit_link = locators.locators.BillingAddressLocators.edit_link
        self.country_select = locators.locators.BillingAddressLocators.country_select
        self.address_input = locators.locators.BillingAddressLocators.address_input
        self.postcode_input = locators.locators.BillingAddressLocators.postcode_input
        self.city_input = locators.locators.BillingAddressLocators.city_input
        self.phone_input = locators.locators.BillingAddressLocators.phone_input
        self.save_address_button = locators.locators.BillingAddressLocators.save_address_button
        self.message = locators.locators.BillingAddressLocators.message

    def open_edit_billing_address(self):
        self.driver.find_element(*self.addresses_link).click()
        self.driver.find_element(*self.edit_link).click()


    def set_personal_data(self, first_name, last_name):
        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)


    def select_country(self, country):
        select = Select(self.driver.find_element(*self.country_select))
        select.select_by_visible_text(country)

    def set_address(self, street, postcode, city):
        self.driver.find_element(*self.address_input).send_keys(street)
        self.driver.find_element(*self.postcode_input).send_keys(postcode)
        self.driver.find_element(*self.city_input).send_keys(city)

    def set_phone_number(self, number):
        self.driver.find_element(*self.phone_input).send_keys(number)

    def save_adress(self):
        self.driver.find_element(*self.save_address_button).click()

    def get_message_text(self):
        return self.driver.find_element(*self.message).text
