import allure
from selenium.webdriver.common.by import By

from page_object_pattern.pages.base_page import BasePage


class SearchResultsPage(BasePage):
    HOTEL_NAMES_XPATH = "//h4[contains(@class, 'list_title')]//b"
    HOTEL_PRICES_XPATH = "//div[contains(@class, 'price_tab')]//b"
    HOTEL_DETAILS_BUTTON_XPATH = "(//button[contains(text(),'Details')])[1]"

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Waiting for search results page to load")
    def wait_until_loaded(self):
        self.wait_for_visible(By.XPATH, self.HOTEL_NAMES_XPATH)

    @allure.step("Getting hotel names from search results")
    def get_hotel_names(self):
        hotels = self.finds(By.XPATH, self.HOTEL_NAMES_XPATH)
        self.attach_screenshot("results")
        return [
            hotel.get_attribute("textContent").strip()
            for hotel in hotels
            if hotel.get_attribute("textContent").strip()
        ]

    @allure.step("Getting hotel prices from search results")
    def get_hotel_prices(self):
        prices = self.finds(By.XPATH, self.HOTEL_PRICES_XPATH)
        return [
            price.get_attribute("textContent").strip()
            for price in prices
            if price.get_attribute("textContent").strip()
        ]

    @allure.step("Clicking first hotel details button")
    def click_hotel_details(self):
        self.click(By.XPATH, self.HOTEL_DETAILS_BUTTON_XPATH)