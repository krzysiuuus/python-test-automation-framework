import allure

from api_tests.data.login_payload import LOGIN_PAYLOAD
from api_tests.utils.auth_api import AuthApi
from api_tests.utils.api_client import ApiClient


@allure.feature("Authentication API")
@allure.story("User login")
class TestLoginApi:

    @allure.title("Verify user can log in")
    def test_login_api(self):

        response = AuthApi.login(LOGIN_PAYLOAD)

        assert response.status_code == 200

        response_body = response.json()

        assert "token" in response_body

        token = response_body["token"]

        ApiClient.set_token(token)