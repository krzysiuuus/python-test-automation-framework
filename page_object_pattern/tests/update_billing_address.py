import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import pytest

from page_object_pattern.pages.billing_address_page import BillingAddressPage
from page_object_pattern.pages.my_account_page import MyAccountPage

@pytest.mark.usefixtures("setup")
class TestUpdateBillingAddress:

    def test_update_billing_address(self):
        email = str(random.randint(0,10000)) + "qwerty@o2.pl"
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.create_account(email, "Qwerty123!@#123")
        billing_address_page = BillingAddressPage(self.driver)
        billing_address_page.open_edit_billing_address()
        billing_address_page.set_personal_data("john", "doe")
        billing_address_page.select_country("Poland")
        billing_address_page.set_address("Kwiatowa 11", "01-001", "Warsaw")
        billing_address_page.set_phone_number('123123123')
        billing_address_page.save_adress()

        assert 'Address changed successfully.' in billing_address_page.get_message_text()