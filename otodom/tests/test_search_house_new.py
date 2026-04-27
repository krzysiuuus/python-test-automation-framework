import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from otodom.pages.search_houses import SearchOtoDomPage
from otodom.pages.search_houses_results import SearchOtoDomResults


@pytest.mark.usefixtures("setup")
class TestHouseSearch:

    @allure.title("This is title")
    @allure.description("This is description")
    def test_house_search(self):
        self.driver.get("https://www.otodom.pl/")
        SearchOtoDomPage(self.driver).accept_cookies()
        SearchOtoDomPage(self.driver).set_city('Stare Babice')
        SearchOtoDomPage(self.driver).set_estate_type('Domy')
        SearchOtoDomPage(self.driver).set_price(1700000)
        SearchOtoDomPage(self.driver).set_size(210)
        SearchOtoDomPage(self.driver).click_search_button()
        SearchOtoDomResults(self.driver).sort_results()
        houses_names = SearchOtoDomResults(self.driver).get_houses_names()

        assert houses_names[3] == 'Skrajny segment✨nowoczesny✨działka 502 mkw✨0%'
        #120-210 metrów
        #działka min 400
        #lokalizacja Izabelin, stare babice
        #cena 1.700.000

    @allure.title("This is title")
    @allure.description("This is description")
    def test_house_search_next(self):
        self.driver.get("https://www.otodom.pl/")
        SearchOtoDomPage(self.driver).accept_cookies()
        SearchOtoDomPage(self.driver).set_city('Izabelin')
        SearchOtoDomPage(self.driver).set_estate_type('Domy')
        SearchOtoDomPage(self.driver).set_price(1700000)
        SearchOtoDomPage(self.driver).set_size(210)
        SearchOtoDomPage(self.driver).click_search_button()
        SearchOtoDomResults(self.driver).sort_results()
        houses_names = SearchOtoDomResults(self.driver).get_houses_names()
        assert houses_names[0] == 'Segment w zabudowie bliźniaczej 129 m² DZIAŁKA 500m2 gm. Izabelin FVAT'