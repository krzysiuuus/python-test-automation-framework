import allure

from api_tests.data.auth_payload import LOGIN_PAYLOAD
from api_tests.utils.api_client import ApiClient
from api_tests.utils.auth_api import AuthApi
from core.config import REQRES_BASE_URL


@allure.feature("Authentication API")
class TestAuthentication:

    @allure.title("Verify authenticated user can access profile")
    def test_authenticated_user_can_access_profile(self):
        login_response = AuthApi.login(LOGIN_PAYLOAD)

        assert login_response.status_code == 200

        login_body = login_response.json()

        magic_token = login_body["data"]["token"]

        verify_response = AuthApi.verify({
            "token": magic_token
        })

        assert verify_response.status_code == 200

        verify_body = verify_response.json()

        session_token = verify_body["data"]["session_token"]

        ApiClient.set_token(session_token)

        me_response = ApiClient.get(
            REQRES_BASE_URL,
            "/app-users/me"
        )

        assert me_response.status_code == 200