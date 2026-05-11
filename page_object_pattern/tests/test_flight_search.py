import allure
import pytest

from page_object_pattern.pages.flight_book import FlightBookPage
from page_object_pattern.pages.flight_invoice import FlightInvoicePage
from page_object_pattern.pages.flight_list import FlightListPage
from page_object_pattern.pages.flight_search import SearchFlightPage

from page_object_pattern.tests.test_data.flight_data import TEST_DATA


@pytest.mark.usefixtures("setup")
class TestFlightSearch:

    @allure.title("User can search and book flight")
    @allure.description("Test verifies complete flight booking flow")
    def test_flight_search(self, flight_date_range):
        self.driver.get("http://www.kurs-selenium.pl/demo/")

        flight_search_page = SearchFlightPage(self.driver)

        flight_search_page.switch_to_flights()
        flight_search_page.select_round_trip()

        flight_search_page.set_departure_city(TEST_DATA["departure_city"])
        flight_search_page.set_arrival_city(TEST_DATA["arrival_city"])

        flight_search_page.set_date_range(
            flight_date_range["check_in"],
            flight_date_range["check_out"]
        )

        flight_search_page.set_travellers(*TEST_DATA["travellers"])

        flight_search_page.perform_search()

        assert self.driver.title == "Flights List"

        flight_list_page = FlightListPage(self.driver)

        flight_list_page.is_loaded()
        flight_list_page.search_only_specific_airline(TEST_DATA["airline"])
        flight_list_page.check_more_details()
        flight_list_page.click_book_button()

        assert self.driver.title == "PHPTRAVELS | Travel Technology Partner"

        flight_book_page = FlightBookPage(self.driver)

        flight_book_page.wait_until_loaded()
        flight_book_page.enter_name()
        flight_book_page.select_country()
        flight_book_page.enter_note()
        flight_book_page.click_confirm_booking()

        flight_invoice_page = FlightInvoicePage(self.driver)

        flight_invoice_page.is_loaded()

        invoice = flight_invoice_page.verify_invoice()

        assert invoice["name"] == TEST_DATA["user"]["name"]
        assert invoice["address"] == TEST_DATA["user"]["address"]
        assert invoice["phone"] == TEST_DATA["user"]["phone"]
        assert invoice["departure_city"] == TEST_DATA["invoice"]["departure_city"]
        assert invoice["arrival_city"] == TEST_DATA["invoice"]["arrival_city"]
        assert "The test is here old man" in invoice["note"]

        flight_invoice_page.enter_card()

        assert TEST_DATA["payment_error"] in flight_invoice_page.verify_incorrect_card()