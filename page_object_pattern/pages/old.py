import logging
import pytest
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class SearchFlightPage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    @allure.step("Switch to flights")
    def switch_to_flights(self):
        self.logger.info("Switching to flights")
        self.driver.find_element(By.XPATH, "//span[text()='Flights  ']").click()

    @allure.step("Select round trip")
    def select_round_trip(self):
        self.logger.info("Selecting round trip")
        self.driver.find_element(By.XPATH, "//div[@class='iradio_square-grey']").click()

    @allure.step("Setting departure city to '{1}'")
    def set_departure_city(self, city):
        self.logger.info("setting departure city {}".format(city))
        self.driver.find_element(By.XPATH, "//span[text()='Enter City Or Airport']").click()
        self.driver.find_element(By.XPATH, "//div[@id='select2-drop']//input").send_keys(city)
        self.driver.find_element(By.XPATH, "//span[text()='{}']".format(city)).click()
        allure.attach(self.driver.get_screenshot_as_png(), name="set_departure_city", attachment_type=AttachmentType.PNG)

    @allure.step("Setting arrival city to '{1}'")
    def set_arrival_city(self, city):
        self.logger.info("setting arrival city {}".format(city))
        self.driver.find_element(By.XPATH, "//span[text()='Enter City Or Airport']").click()
        self.driver.find_element(By.XPATH, "//div[@id='select2-drop']//input").send_keys(city)
        self.driver.find_element(By.XPATH, "//span[text()='{}']".format(city)).click()
        allure.attach(self.driver.get_screenshot_as_png(), name="set_arrival_city", attachment_type=AttachmentType.PNG)

    @allure.step("Setting date from '{1}' to '{2}'")
    def set_date_range(self, check_in, check_out):
        self.logger.info("setting check in {checkin} and check out {checkout}".format(checkin=check_in, checkout=check_out))
        self.driver.find_element(By.NAME, "departure").send_keys(check_in)
        self.driver.find_element(By.NAME, "arrival").send_keys(check_out)
        allure.attach(self.driver.get_screenshot_as_png(), name="set date range", attachment_type=AttachmentType.PNG)

    @allure.step("Setting travellers adults '{1}', kids '{2}, infants {3}'")
    def set_travellers(self, adults, child, infant):
        wait = WebDriverWait(self.driver, 5, 0.5)
        self.logger.info("setting travellers {adults}, kids {child} and infants {infant}".format(adults=adults, child=child, infant=infant))
        self.driver.find_element(By.NAME, "totalManualPassenger").click()
        wait.until(expected_conditions.visibility_of_element_located((By.NAME, "madult")))
        self.driver.find_element(By.NAME, "madult").click()
        auto_select = Select(self.driver.find_element(By.XPATH, "//select[@name='madult']"))
        auto_select.select_by_value(adults)
        self.driver.find_element(By.NAME, "mchildren").click()
        Select(self.driver.find_element(By.XPATH, "//select[@name='mchildren']")).select_by_value(child)
        self.driver.find_element(By.NAME, "minfant").click()
        Select(self.driver.find_element(By.XPATH, "//select[@name='minfant']")).select_by_value(infant)
        self.driver.find_element(By.ID, "sumManualPassenger").click()
        allure.attach(self.driver.get_screenshot_as_png(), name="set travellers", attachment_type=AttachmentType.PNG)

    def perform_search(self):
        self.logger.info("performing search")
        self.driver.find_element(By.XPATH, "//div[@class='bgfade col-md-3 col-xs-12 search-button']//button").click()








import logging
import pytest
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FlightListPage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    def is_loaded(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "checkair"))
        )
        return True

    @allure.step("Switch to flights")
    def search_only_specific_airline(self, airline):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(By.ID, "checkair{}".format(airline)))
        self.driver.find_element(By.XPATH, "//input[@value='{}']/following-sibling::ins[contains(@class,'iCheck-helper')]".format(airline)).click()

    @allure.step("Check More Details")
    def check_more_details(self):
        self.driver.find_element(By.XPATH, "//a[text()='More Details']").click()
        desc = self.driver.find_element(By.XPATH, "//p[contains(@class, 'main-title go-right')]")
        desc_desc = [desc.get_attribute("textContent")]
        print("Hotel name: " + str(desc_desc))

    @allure.step("Click book button")
    def click_book_button(self):
        self.driver.find_element(By.XPATH, "//button[@id='bookbtn']").click()
