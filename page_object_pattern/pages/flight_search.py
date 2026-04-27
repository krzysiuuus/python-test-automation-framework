import logging
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from page_object_pattern.pages.base_page import BasePage


class SearchFlightPage(BasePage):
    FLIGHTS_TAB_XPATH = "//span[text()='Flights  ']"
    ROUND_TRIP_RADIO_XPATH = "//div[@class='iradio_square-grey']"

    CITY_DROPDOWN_XPATH = "//span[text()='Enter City Or Airport']"
    CITY_SEARCH_INPUT_XPATH = "//div[@id='select2-drop']//input"
    CITY_OPTION_XPATH = "//span[text()='{city}']"

    DEPARTURE_DATE_INPUT_NAME = "departure"
    ARRIVAL_DATE_INPUT_NAME = "arrival"

    PASSENGER_INPUT_NAME = "totalManualPassenger"
    ADULT_SELECT_NAME = "madult"
    CHILD_SELECT_NAME = "mchildren"
    INFANT_SELECT_NAME = "minfant"
    PASSENGER_SUMMARY_BUTTON_ID = "sumManualPassenger"

    SEARCH_BUTTON_XPATH = "//div[@class='bgfade col-md-3 col-xs-12 search-button']//button"

    def __init__(self, driver):
        super().__init__(driver)
        self.logger = logging.getLogger(__name__)

    @allure.step("Switch to flights")
    def switch_to_flights(self):
        self.logger.info("Switching to flights")
        self.click(By.XPATH, self.FLIGHTS_TAB_XPATH)
        self.attach_screenshot("switch_to_flights")

    @allure.step("Select round trip")
    def select_round_trip(self):
        self.logger.info("Selecting round trip")
        self.click(By.XPATH, self.ROUND_TRIP_RADIO_XPATH)
        self.attach_screenshot("select_round_trip")

    @allure.step("Setting departure city to '{city}'")
    def set_departure_city(self, city):
        self.logger.info(f"Setting departure city: {city}")
        self.click(By.XPATH, self.CITY_DROPDOWN_XPATH)
        self.type(By.XPATH, self.CITY_SEARCH_INPUT_XPATH, city)
        self.click(By.XPATH, self.CITY_OPTION_XPATH.format(city=city))
        self.attach_screenshot("set_departure_city")

    @allure.step("Setting arrival city to '{city}'")
    def set_arrival_city(self, city):
        self.logger.info(f"Setting arrival city: {city}")
        self.click(By.XPATH, self.CITY_DROPDOWN_XPATH)
        self.type(By.XPATH, self.CITY_SEARCH_INPUT_XPATH, city)
        self.click(By.XPATH, self.CITY_OPTION_XPATH.format(city=city))
        self.attach_screenshot("set_arrival_city")

    @allure.step("Setting date from '{check_in}' to '{check_out}'")
    def set_date_range(self, check_in, check_out):
        self.logger.info(f"Setting departure date: {check_in}, arrival date: {check_out}")
        self.type(By.NAME, self.DEPARTURE_DATE_INPUT_NAME, check_in)
        self.type(By.NAME, self.ARRIVAL_DATE_INPUT_NAME, check_out)
        self.attach_screenshot("set_date_range")

    @allure.step("Setting travellers adults '{adults}', kids '{child}', infants '{infant}'")
    def set_travellers(self, adults, child, infant):
        self.logger.info(
            f"Setting travellers: adults={adults}, child={child}, infant={infant}"
        )

        self.click(By.NAME, self.PASSENGER_INPUT_NAME)
        self.wait_for_visible(By.NAME, self.ADULT_SELECT_NAME)

        adult_select = self.find(By.NAME, self.ADULT_SELECT_NAME)
        Select(adult_select).select_by_value(adults)

        child_select = self.find(By.NAME, self.CHILD_SELECT_NAME)
        Select(child_select).select_by_value(child)

        infant_select = self.find(By.NAME, self.INFANT_SELECT_NAME)
        Select(infant_select).select_by_value(infant)

        self.click(By.ID, self.PASSENGER_SUMMARY_BUTTON_ID)
        self.attach_screenshot("set_travellers")

    @allure.step("Perform flight search")
    def perform_search(self):
        self.logger.info("Performing flight search")
        self.click(By.XPATH, self.SEARCH_BUTTON_XPATH)
        self.attach_screenshot("perform_search")