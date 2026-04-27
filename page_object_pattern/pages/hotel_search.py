import logging
import allure
from selenium.webdriver.common.by import By

from page_object_pattern.pages.base_page import BasePage


class SearchHotelPage(BasePage):
    SEARCH_HOTEL_SPAN_XPATH = "//span[text()='Search by Hotel or City Name']"
    SEARCH_HOTEL_INPUT_XPATH = "//div[@id='select2-drop']//input"
    LOCATION_MATCH_SPAN_XPATH = "//span[text()='{city}']"
    CHECK_IN_INPUT_NAME = "checkin"
    CHECK_OUT_INPUT_NAME = "checkout"
    TRAVELLERS_INPUT_ID = "travellersInput"
    ADULT_INPUT_ID = "adultInput"
    CHILD_INPUT_ID = "childInput"
    SEARCH_BUTTON_XPATH = "//button[text()=' Search']"

    def __init__(self, driver):
        super().__init__(driver)
        self.logger = logging.getLogger(__name__)

    @allure.step("Setting city name to '{city}'")
    def set_city(self, city):
        self.logger.info(f"Setting city: {city}")
        self.click(By.XPATH, self.SEARCH_HOTEL_SPAN_XPATH)
        self.type(By.XPATH, self.SEARCH_HOTEL_INPUT_XPATH, city)
        self.click(By.XPATH, self.LOCATION_MATCH_SPAN_XPATH.format(city=city))
        self.attach_screenshot("set_city")

    @allure.step("Setting date from '{check_in}' to '{check_out}'")
    def set_date_range(self, check_in, check_out):
        self.logger.info(f"Setting check-in: {check_in}, check-out: {check_out}")
        self.type(By.NAME, self.CHECK_IN_INPUT_NAME, check_in)
        self.type(By.NAME, self.CHECK_OUT_INPUT_NAME, check_out)
        self.attach_screenshot("set_date_range")

    @allure.step("Setting travellers adults '{adults}' and kids '{child}'")
    def set_travellers(self, adults, child):
        self.logger.info(f"Setting travellers: adults={adults}, child={child}")
        self.click(By.ID, self.TRAVELLERS_INPUT_ID)
        self.type(By.ID, self.ADULT_INPUT_ID, adults)
        self.type(By.ID, self.CHILD_INPUT_ID, child)
        self.attach_screenshot("set_travellers")

    @allure.step("Performing hotel search")
    def perform_search(self):
        self.logger.info("Performing hotel search")
        self.click(By.XPATH, self.SEARCH_BUTTON_XPATH)