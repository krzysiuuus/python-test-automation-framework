import logging
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from page_object_pattern.pages.base_page import BasePage


class FlightBookPage(BasePage):
    FIRST_NAME_INPUT_XPATH = "//input[@name='firstname']"
    LAST_NAME_INPUT_XPATH = "//input[@name='lastname']"
    EMAIL_INPUT_XPATH = "//input[@name='email']"
    CONFIRM_EMAIL_INPUT_XPATH = "//input[@name='confirmemail']"
    PHONE_INPUT_XPATH = "//input[@name='phone']"
    ADDRESS_INPUT_XPATH = "//input[@name='address']"

    COUNTRY_DROPDOWN_XPATH = "//a[@class='select2-choice']"
    COUNTRY_SEARCH_INPUT_XPATH = "//div[@class='select2-search']//input"
    COUNTRY_OPTION_XPATH = "//span[text()='{country}']"

    NOTE_LABEL_XPATH = "//div[@class='panel-heading']//label"
    ADDITIONAL_NOTES_TEXTAREA_XPATH = "//textarea[@name='additionalnotes']"

    CONFIRM_BOOKING_BUTTON_XPATH = "//button[@name='guest']"

    def __init__(self, driver):
        super().__init__(driver)
        self.logger = logging.getLogger(__name__)

    @allure.step("Waiting for flight booking page to load")
    def wait_until_loaded(self):
        self.wait_for_visible(By.XPATH, self.FIRST_NAME_INPUT_XPATH)

    @allure.step("Enter guest personal data")
    def enter_name(self):
        self.logger.info("Entering guest personal data")
        self.type(By.XPATH, self.FIRST_NAME_INPUT_XPATH, "Anon")
        self.type(By.XPATH, self.LAST_NAME_INPUT_XPATH, "Anonski")
        self.type(By.XPATH, self.EMAIL_INPUT_XPATH, "Anon@non.pl")
        self.type(By.XPATH, self.CONFIRM_EMAIL_INPUT_XPATH, "Anon@non.pl")
        self.type(By.XPATH, self.PHONE_INPUT_XPATH, "234567246")
        self.type(By.XPATH, self.ADDRESS_INPUT_XPATH, "Anon 24/7")
        self.attach_screenshot("enter_name")

    @allure.step("Select country '{country}'")
    def select_country(self, country="Poland"):
        self.logger.info(f"Selecting country: {country}")
        self.click(By.XPATH, self.COUNTRY_DROPDOWN_XPATH)
        self.type(By.XPATH, self.COUNTRY_SEARCH_INPUT_XPATH, country)
        self.click(By.XPATH, self.COUNTRY_OPTION_XPATH.format(country=country))
        self.attach_screenshot("select_country")

    @allure.step("Enter additional note")
    def enter_note(self, note="The test is here old man"):
        self.logger.info("Entering additional note")
        self.click(By.XPATH, self.NOTE_LABEL_XPATH)
        self.type(By.XPATH, self.ADDITIONAL_NOTES_TEXTAREA_XPATH, note)
        self.attach_screenshot("enter_note")

    @allure.step("Click confirm booking")
    def click_confirm_booking(self):
        self.logger.info("Clicking confirm booking")
        confirm_button = self.find(By.XPATH, self.CONFIRM_BOOKING_BUTTON_XPATH)
        self.driver.execute_script("arguments[0].scrollIntoView();", confirm_button)
        self.click(By.XPATH, self.CONFIRM_BOOKING_BUTTON_XPATH)
        self.attach_screenshot("after_confirm_booking")