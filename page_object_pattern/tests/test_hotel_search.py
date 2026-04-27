import allure
import pytest
from page_object_pattern.pages.flight_book import FlightBookPage
from page_object_pattern.pages.flight_invoice import FlightInvoicePage
from page_object_pattern.pages.hotel_details import HotelDetailsPage
from page_object_pattern.pages.hotel_invoice import HotelInvoicePage
from page_object_pattern.pages.hotel_search import SearchHotelPage
from page_object_pattern.pages.hotel_search_results import SearchResultsPage
from test_data.hotel_data import TEST_DATA



@pytest.mark.usefixtures("setup")
class TestHotelSearch:

    @allure.title("This is title")
    @allure.description("This is description")
    def test_hotel_search(self, date_range):
        self.driver.get("http://www.kurs-selenium.pl/demo/")
        search_hotel_page = SearchHotelPage(self.driver)
        search_hotel_page.set_city(TEST_DATA["city"])
        search_hotel_page.set_date_range(
            date_range["check_in"],
            date_range["check_out"]
        )
        search_hotel_page.set_travellers(*TEST_DATA["travellers"])
        search_hotel_page.perform_search()
        results_page = SearchResultsPage(self.driver)
        results_page.wait_until_loaded()
        hotel_names = results_page.get_hotel_names()
        price_values = results_page.get_hotel_prices()
        for hotel in TEST_DATA["expected_hotels"]:
            assert hotel in hotel_names
        expected_prices = [
            "$22",
            "$50",
            "$80",
            "$150"
        ]
        assert price_values == expected_prices
        results_page.click_hotel_details()
        hotel_details = HotelDetailsPage(self.driver)
        hotel_details.wait_until_loaded()
        hotel_details.modify_dates_guests()
        hotel_details.select_room_click_book()
        flight_book = FlightBookPage(self.driver)
        flight_book.wait_until_loaded()
        flight_book.enter_name()
        flight_book.select_country()
        flight_book.enter_note()
        flight_book.click_confirm_booking()
        invoice = HotelInvoicePage(self.driver).verify_invoice()
        assert invoice["name"] == TEST_DATA["user"]["name"]
        assert invoice["address"] == TEST_DATA["user"]["address"]
        assert invoice["phone"] == TEST_DATA["user"]["phone"]
        assert invoice["hotel"] == "Jumeirah Beach Hotel"
        assert invoice["city"] == TEST_DATA["city"]
        assert "The test is here old man" in invoice["note"]
        flight_invoice_page = FlightInvoicePage(self.driver)
        flight_invoice_page.enter_card()
        assert "THE MERCHANT LOGIN ID OR PASSWORD IS INVALID OR THE ACCOUNT IS INACTIVE." in flight_invoice_page.verify_incorrect_card()
