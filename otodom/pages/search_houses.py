import logging
import time

import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class SearchOtoDomPage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.cookies_css = (By.CSS_SELECTOR, "#onetrust-accept-btn-handler")
        self.city_input_click_xpath = (By.XPATH, "//input[@placeholder='Wpisz lokalizację']")
        self.city_input_id = (By.ID, "location-search-input")
        self.city_select_click_class = (By.CLASS_NAME, "css-1ywedzp")
        self.estate_dropdown_id = (By.ID, "estate-dropdown")
        self.estate_type_xpath = (By.XPATH, "//span[text()='Domy']")
        self.price_max_id = (By.ID, "priceMax")
        self.size_max_id = (By.ID, "areaMax")
        self.search_button_id = (By.ID, "search-form-submit")

    @allure.step("Accepting cookies")
    def accept_cookies(self):
        wait = WebDriverWait(self.driver, 10, 0.5)
        wait.until(expected_conditions.visibility_of_element_located(self.cookies_css))
        self.driver.find_element(*self.cookies_css).click()

    @allure.step("Setting city name to '{1}'")
    def set_city(self, city):
        self.logger.info("setting city {}".format(city))
        wait = WebDriverWait(self.driver, 10, 0.5)
        self.driver.find_element(*self.city_input_click_xpath).click()
        wait.until(expected_conditions.visibility_of_element_located(self.city_input_id))
        self.driver.find_element(*self.city_input_id).send_keys(city)
        wait.until(expected_conditions.visibility_of_element_located(self.city_select_click_class))
        self.driver.find_element(*self.city_select_click_class).click()

    @allure.step("Setting estate type to '{1}'")
    def set_estate_type(self, typee):
        self.logger.info("setting estate type {}".format(typee))
        wait = WebDriverWait(self.driver, 10, 0.5)
        self.driver.find_element(*self.estate_dropdown_id).click()
        self.driver.find_element(*self.estate_type_xpath).click()

    @allure.step("Setting price maximum to '{1}'")
    def set_price(self, max):
        self.logger.info("setting price maximum to {}".format(max))
        wait = WebDriverWait(self.driver, 10, 0.5)
        self.driver.find_element(*self.price_max_id).send_keys(max)

    @allure.step("Setting size maximum to '{1}'")
    def set_size(self, max):
        self.logger.info("setting size maximum to {}".format(max))
        wait = WebDriverWait(self.driver, 10, 0.5)
        self.driver.find_element(*self.size_max_id).send_keys(max)

    @allure.step("Clicking search button")
    def click_search_button(self):
        self.logger.info("clicking search button")
        wait = WebDriverWait(self.driver, 10, 0.5)
        time.sleep(1)
        self.driver.find_element(*self.search_button_id).click()
        allure.attach(self.driver.get_screenshot_as_png(), name="set_city", attachment_type=AttachmentType.PNG)