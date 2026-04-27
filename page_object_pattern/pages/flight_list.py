import logging
import allure
from selenium.webdriver.common.by import By

from page_object_pattern.pages.base_page import BasePage


class FlightListPage(BasePage):
    AIRLINE_CHECKBOX_ID_TEMPLATE = "checkair{airline}"
    AIRLINE_CHECKBOX_HELPER_XPATH = "//input[contains(@value,'{airline}')]/following-sibling::ins[contains(@class,'iCheck-helper')]"

    MORE_DETAILS_LINK_XPATH = "//a[text()='More Details']"
    FLIGHT_DESCRIPTION_XPATH = "//p[contains(@class, 'main-title go-right')]"

    BOOK_BUTTON_XPATH = "//button[@id='bookbtn']"

    def __init__(self, driver):
        super().__init__(driver)
        self.logger = logging.getLogger(__name__)

    @allure.step("Waiting for flight list page to load")
    def is_loaded(self):
        self.wait_for_visible(By.XPATH, self.MORE_DETAILS_LINK_XPATH)
        return True

    @allure.step("Filter results by airline '{airline}'")
    def search_only_specific_airline(self, airline):
        self.logger.info(f"Filtering results by airline: {airline}")

        airline_input_xpath = f"//input[normalize-space(@value)='{airline}']"
        airline_helper_xpath = f"{airline_input_xpath}/following-sibling::ins[contains(@class,'iCheck-helper')]"

        self.wait.until(
            lambda driver: len(driver.find_elements(By.XPATH, airline_input_xpath)) > 0
        )
        self.wait.until(
            lambda driver: len(driver.find_elements(By.XPATH, airline_helper_xpath)) > 0
        )

        airline_input = self.driver.find_element(By.XPATH, airline_input_xpath)
        airline_helper = self.driver.find_element(By.XPATH, airline_helper_xpath)

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            airline_input
        )

        self.driver.execute_script("arguments[0].click();", airline_helper)

        self.attach_screenshot("search_only_specific_airline")

    @allure.step("Check more details")
    def check_more_details(self):
        self.logger.info("Checking more flight details")

        self.click(By.XPATH, self.MORE_DETAILS_LINK_XPATH)
        desc = self.get_text(By.XPATH, self.FLIGHT_DESCRIPTION_XPATH).strip()

        self.attach_screenshot("check_more_details")
        return desc

    @allure.step("Click book button")
    def click_book_button(self):
        self.logger.info("Clicking flight book button")

        self.click(By.XPATH, self.BOOK_BUTTON_XPATH)
        self.attach_screenshot("click_book_button")