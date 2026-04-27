import logging
import allure
from selenium.webdriver.common.by import By

from page_object_pattern.pages.base_page import BasePage


class HotelInvoicePage(BasePage):
    INVOICE_TITLE_XPATH = "//div[text()='Invoice']"
    NAME_XPATH = "//div[2]/table/tbody/tr/td/div[2]"
    ADDRESS_XPATH = "//div[2]/table/tbody/tr/td/div[3]"
    PHONE_XPATH = "//div[2]/table/tbody/tr/td/div[4]"
    HOTEL_NAME_XPATH = "(//table[1]/tbody/tr[1]/td[1])[5]"
    ARRIVAL_CITY_XPATH = "//table[1]/tbody/tr[1]/td[2]"
    NOTE_XPATH = "//div[@class='panel-body']"

    def __init__(self, driver):
        super().__init__(driver, timeout=25)
        self.logger = logging.getLogger(__name__)

    @allure.step("Checking if hotel invoice page is loaded")
    def is_loaded(self):
        self.wait_for_visible(By.XPATH, self.INVOICE_TITLE_XPATH)
        return True

    @allure.step("Verifying hotel invoice")
    def verify_invoice(self):
        self.logger.info("Verifying invoice")

        self.wait_for_visible(By.XPATH, self.INVOICE_TITLE_XPATH)
        self.attach_screenshot("hotel_invoice")

        return {
            "name": self.get_text(By.XPATH, self.NAME_XPATH).strip(),
            "address": self.get_text(By.XPATH, self.ADDRESS_XPATH).strip(),
            "phone": self.get_text(By.XPATH, self.PHONE_XPATH).strip(),
            "hotel": self.get_text(By.XPATH, self.HOTEL_NAME_XPATH).strip(),
            "city": self.get_text(By.XPATH, self.ARRIVAL_CITY_XPATH).strip(),
            "note": self.get_text(By.XPATH, self.NOTE_XPATH).strip()
        }