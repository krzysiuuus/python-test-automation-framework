import logging
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

from page_object_pattern.pages.base_page import BasePage


class HotelDetailsPage(BasePage):
    AVAILABLE_ROOMS_TITLE_XPATH = "//div[text()='Available Rooms']"
    CHILD_SELECT_XPATH = "(//select[@name='child'])[2]"
    MODIFY_BUTTON_XPATH = "(//input[@value='Modify'])[2]"
    BOOK_NOW_BUTTON_XPATH = "//button[contains(@class,'book_button') and normalize-space()='Book Now']"
    ROOM_CHECKBOX_XPATH = "//div[@class='control__indicator']"

    def __init__(self, driver):
        super().__init__(driver)
        self.logger = logging.getLogger(__name__)

    @allure.step("Waiting for hotel details page to load")
    def wait_until_loaded(self):
        self.wait_for_visible(By.XPATH, self.AVAILABLE_ROOMS_TITLE_XPATH)

    @allure.step("Modify dates or guests")
    def modify_dates_guests(self):
        self.logger.info("Modifying dates or guests")

        element = self.find(By.XPATH, self.AVAILABLE_ROOMS_TITLE_XPATH)
        ActionChains(self.driver).move_to_element(element).perform()

        child_select = self.find(By.XPATH, self.CHILD_SELECT_XPATH)
        Select(child_select).select_by_value("2")

        self.click(By.XPATH, self.MODIFY_BUTTON_XPATH)
        self.attach_screenshot("modify_dates_guests")

    @allure.step("Select room and click book")
    def select_room_click_book(self):
        self.logger.info("Selecting room and clicking book")

        book_now_button = self.find(By.XPATH, self.BOOK_NOW_BUTTON_XPATH)
        ActionChains(self.driver).move_to_element(book_now_button).perform()

        self.click(By.XPATH, self.ROOM_CHECKBOX_XPATH)
        self.click(By.XPATH, self.BOOK_NOW_BUTTON_XPATH)
        self.attach_screenshot("select_room_click_book")