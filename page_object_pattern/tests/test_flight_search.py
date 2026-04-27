import allure
import pytest

from page_object_pattern.pages.flight_book import FlightBookPage
from page_object_pattern.pages.flight_invoice import FlightInvoicePage
from page_object_pattern.pages.flight_list import FlightListPage
from page_object_pattern.pages.flight_search import SearchFlightPage


@pytest.mark.usefixtures("setup")
class TestFlightSearch:

    @allure.title("This is search flight test")
    @allure.description("This is description of search flight test")
    def test_flight_search(self):
        self.driver.get("http://www.kurs-selenium.pl/demo/")

        flight_search_page = SearchFlightPage(self.driver)
        flight_search_page.switch_to_flights()
        flight_search_page.select_round_trip()
        flight_search_page.set_departure_city("Warsaw")
        flight_search_page.set_arrival_city("Dubai")
        flight_search_page.set_date_range("2026-01-24", "2026-01-31")
        flight_search_page.set_travellers("2", "2", "2")
        flight_search_page.perform_search()

        assert self.driver.title == "Flights List"

        flight_list_page = FlightListPage(self.driver)
        flight_list_page.is_loaded()
        flight_list_page.search_only_specific_airline("Air Arabia")
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

        assert invoice["name"] == "ANON ANONSKI"
        assert invoice["address"] == "ANON 24/7"
        assert invoice["phone"] == "234567246"
        assert invoice["departure_city"] == "Warsaw Intl Arpt"
        assert invoice["arrival_city"] == "Dubai Intl Arpt"
        assert "The test is here old man" in invoice["note"]

        flight_invoice_page.enter_card()

        assert (
            "THE MERCHANT LOGIN ID OR PASSWORD IS INVALID OR THE ACCOUNT IS INACTIVE."
            in flight_invoice_page.verify_incorrect_card()
        )