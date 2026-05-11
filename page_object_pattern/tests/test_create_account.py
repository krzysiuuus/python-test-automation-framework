import allure
import pytest
from page_object_pattern.utils.data_generator import generate_email
from page_object_pattern.pages.my_account_page import MyAccountPage
from test_data.user_data import DEFAULT_PASSWORD


@pytest.mark.usefixtures("setup")
class TestCreateAccount:

    @allure.title("User can create account")
    @allure.description("Verify user can create account successfully")
    def test_user_can_create_account(self):
        email = generate_email()
        password = DEFAULT_PASSWORD
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.create_account(email, password)
        assert my_account_page.is_logout_link_displayed()

    @allure.title("User cannot create account with existing email")
    @allure.description("Verify error message for duplicate email")
    def test_user_cannot_create_account_with_existing_email(self):
        email = generate_email()
        password = DEFAULT_PASSWORD
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        # create account first time
        my_account_page.create_account(email, password)
        assert my_account_page.is_logout_link_displayed()
        # logout
        my_account_page.logout()
        # try to create same account again
        my_account_page.open_page()
        my_account_page.create_account(email, password)
        expected_message = (
            "An account is already registered with your email address."
        )
        assert expected_message in my_account_page.get_error_message()

