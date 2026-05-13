import allure
import pytest

from page_object_pattern.pages.billing_address_page import BillingAddressPage
from page_object_pattern.pages.my_account_page import MyAccountPage
from page_object_pattern.utils.data_generator import generate_email
from page_object_pattern.tests.test_data.user_data import DEFAULT_PASSWORD


@pytest.mark.usefixtures("setup")
class TestUpdateBillingAddress:

    @allure.title("User can update billing address")
    @allure.description("Test verifies user can update billing address successfully")
    def test_update_billing_address(self):
        email = generate_email()
        password = DEFAULT_PASSWORD

        my_account_page = MyAccountPage(self.driver)

        my_account_page.open_page()
        my_account_page.wait_until_loaded()
        my_account_page.create_account(email, password)

        billing_address_page = BillingAddressPage(self.driver)

        billing_address_page.open_edit_billing_address()
        billing_address_page.set_personal_data("john", "doe")
        billing_address_page.select_country("Poland")
        billing_address_page.set_address("Kwiatowa 11", "01-001", "Warsaw")
        billing_address_page.set_phone_number("123123123")
        billing_address_page.save_address()

        assert "Address changed successfully." in billing_address_page.get_message_text()