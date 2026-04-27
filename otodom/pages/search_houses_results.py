import logging
import time

import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class SearchOtoDomResults:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.sorting_dropdown_xpath = (By.XPATH, "//div[text()='Domyślnie']")
        self.sorting_dropdown_newest_xpath = (By.XPATH, "//div[text()='Data dodania: najnowsze']")
        self.houses_names_xpath = (By.XPATH, "//a[contains(@class, 'e13tkx7i0')]//p")


    @allure.step("Sorting results")
    def sort_results(self):
        self.logger.info("sorting results")
        wait = WebDriverWait(self.driver, 10, 0.5)
        wait.until(expected_conditions.visibility_of_element_located(self.sorting_dropdown_xpath))
        self.driver.find_element(*self.sorting_dropdown_xpath).click()
        self.driver.find_element(*self.sorting_dropdown_newest_xpath).click()

    @allure.step("Checking results'")
    def get_houses_names(self):
        time.sleep(2)
        houses = self.driver.find_elements(*self.houses_names_xpath)
        houses_names = [house.get_attribute("textContent") for house in houses]
        for name in houses_names:
            print("House name: " + name)
        return [house.get_attribute("textContent") for house in houses]
