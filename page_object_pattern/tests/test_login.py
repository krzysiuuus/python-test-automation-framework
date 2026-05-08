import pytest
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from page_object_pattern.pages.my_account_page import MyAccountPage


@pytest.mark.usefixtures("setup")
class TestLogIn:

    def test_log_in_passed(self):
        email = f"{random.randint(1000,9999)}qwerty@o2.pl"
        password = "Qwerty123!@#123"
        my_account_page = MyAccountPage(self.driver)
        # create account
        my_account_page.open_page()
        my_account_page.create_account(email, password)
        assert my_account_page.is_logout_link_displayed()
        # logout
        my_account_page.logout()
        # login again
        my_account_page.log_in(email, password)

        assert my_account_page.is_logout_link_displayed()

    def test_log_in_failed(self):
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.log_in("qwerty@o2.pls", "Qwerty123!@#123")

        assert "ERROR: Incorrect username or password." in my_account_page.get_error_message()