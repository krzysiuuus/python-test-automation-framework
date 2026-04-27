import allure
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from page_object_pattern.pages.hotel_search import SearchHotelPage
from page_object_pattern.pages.hotel_search_results import SearchResultsPage
from page_object_pattern.utils.read_excel import ExcelReader


@pytest.mark.usefixtures("setup")
class TestHotelSearch():

    @allure.title("This is title")
    @allure.description("This is description")
    @pytest.mark.parametrize("data", ExcelReader.get_data())
    def test_hotel_search(self, data):
        self.driver.get("http://www.kurs-selenium.pl/demo/")
        search_hotel_page = SearchHotelPage(self.driver)
        search_hotel_page.set_city("Dubai")
        search_hotel_page.set_date_range(data.check_in, data.check_out)
        search_hotel_page.set_travellers("2", "2")
        search_hotel_page.perform_search()
        results_page = SearchResultsPage(self.driver)
        hotel_names = results_page.get_hotel_names()
        price_values = results_page.get_hotel_prices()

        assert hotel_names[0] == 'Jumeirah Beach Hotel'
        assert hotel_names[1] == 'Oasis Beach Tower'
        assert hotel_names[2] == 'Rose Rayhaan Rotana'
        assert hotel_names[3] == 'Hyatt Regency Perth'

        assert price_values[0] == '$2'
        assert price_values[1] == '$50'
        assert price_values[2] == '$80'
        assert price_values[3] == '$150'
