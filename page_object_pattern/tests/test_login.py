import allure
import pytest

from page_object_pattern.pages.my_account_page import MyAccountPage
from page_object_pattern.utils.data_generator import generate_email
from test_data.user_data import DEFAULT_PASSWORD


@pytest.mark.usefixtures("setup")
class TestLogIn:

    @allure.title("User can log in with valid credentials")
    @allure.description("Test verifies user can create account and log in successfully")
    def test_user_can_log_in(self):
        email = generate_email()
        password = DEFAULT_PASSWORD
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.wait_until_loaded()
        my_account_page.create_account(email, password)
        assert my_account_page.is_logout_link_displayed()
        my_account_page.logout()
        my_account_page.log_in(email, password)
        assert my_account_page.is_logout_link_displayed()

    @allure.title("User cannot log in with invalid credentials")
    @allure.description("Test verifies error message is displayed for invalid login")
    def test_user_cannot_log_in_with_invalid_credentials(self):
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.wait_until_loaded()
        my_account_page.log_in("qwerty@o2.pls", DEFAULT_PASSWORD)
        assert "ERROR: Incorrect username or password." in my_account_page.get_error_message()