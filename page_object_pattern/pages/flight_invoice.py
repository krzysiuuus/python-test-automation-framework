import logging
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from page_object_pattern.pages.base_page import BasePage


class FlightInvoicePage(BasePage):
    INVOICE_CONTAINER_ID = "printablediv"

    PAY_NOW_BUTTON_XPATH = "//button[text()='Pay Now']"

    GATEWAY_SELECT_XPATH = "//select[@name='gateway']"
    FIRST_NAME_INPUT_XPATH = "//input[@name='firstname']"
    LAST_NAME_INPUT_XPATH = "//input[@name='lastname']"
    CARD_NUMBER_INPUT_XPATH = "//input[@name='cardnum']"
    EXP_MONTH_SELECT_XPATH = "//select[@name='expMonth']"
    CVV_INPUT_XPATH = "//input[@name='cvv']"
    SUBMIT_PAYMENT_BUTTON_XPATH = "//button[@type='submit']"

    INCORRECT_CARD_MESSAGE_XPATH = "//*[@id='body-section']/div[1]/div[2]/div[1]"

    NAME_XPATH = "//div[2]/table/tbody/tr/td/div[2]"
    ADDRESS_XPATH = "//div[2]/table/tbody/tr/td/div[3]"
    PHONE_XPATH = "//div[2]/table/tbody/tr/td/div[4]"
    DEPARTURE_CITY_XPATH = "//table[2]/tbody/tr[2]/td[3]"
    ARRIVAL_CITY_XPATH = "//table[2]/tbody/tr[3]/td[3]"
    NOTE_XPATH = "//div[@class='panel-body']"

    def __init__(self, driver):
        super().__init__(driver, timeout=20)
        self.logger = logging.getLogger(__name__)

    @allure.step("Checking if flight invoice page is loaded")
    def is_loaded(self):
        self.wait_for_visible(By.ID, self.INVOICE_CONTAINER_ID)
        self.attach_screenshot("flight_invoice_loaded")
        return True

    @allure.step("Verifying flight invoice")
    def verify_invoice(self):
        self.logger.info("Verifying flight invoice")

        self.wait_for_visible(By.ID, self.INVOICE_CONTAINER_ID)
        self.attach_screenshot("flight_invoice")

        return {
            "name": self.get_text(By.XPATH, self.NAME_XPATH).strip(),
            "address": self.get_text(By.XPATH, self.ADDRESS_XPATH).strip(),
            "phone": self.get_text(By.XPATH, self.PHONE_XPATH).strip(),
            "departure_city": self.get_text(By.XPATH, self.DEPARTURE_CITY_XPATH).strip(),
            "arrival_city": self.get_text(By.XPATH, self.ARRIVAL_CITY_XPATH).strip(),
            "note": self.get_text(By.XPATH, self.NOTE_XPATH).strip()
        }

    @allure.step("Enter payment card data")
    def enter_card(self):
        self.logger.info("Entering card data")

        pay_now_button = self.wait_for_clickable(By.XPATH, self.PAY_NOW_BUTTON_XPATH)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            pay_now_button
        )
        pay_now_button.click()

        self.wait_for_visible(By.XPATH, self.GATEWAY_SELECT_XPATH)

        Select(self.find(By.XPATH, self.GATEWAY_SELECT_XPATH)).select_by_value("authorize")

        self.type(By.XPATH, self.FIRST_NAME_INPUT_XPATH, "Anon")
        self.type(By.XPATH, self.LAST_NAME_INPUT_XPATH, "Anonski")
        self.type(By.XPATH, self.CARD_NUMBER_INPUT_XPATH, "1111222233334444")

        Select(self.find(By.XPATH, self.EXP_MONTH_SELECT_XPATH)).select_by_value("12")

        self.type(By.XPATH, self.CVV_INPUT_XPATH, "123")
        self.click(By.XPATH, self.SUBMIT_PAYMENT_BUTTON_XPATH)

        self.attach_screenshot("enter_card")

    @allure.step("Verify incorrect card message")
    def verify_incorrect_card(self):
        self.logger.info("Verifying incorrect card message")

        self.wait_for_visible(By.XPATH, self.INCORRECT_CARD_MESSAGE_XPATH)
        self.attach_screenshot("incorrect_card_message")

        return self.get_text(By.XPATH, self.INCORRECT_CARD_MESSAGE_XPATH).strip()