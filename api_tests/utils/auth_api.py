from api_tests.utils.api_client import ApiClient
from core.config import REQRES_BASE_URL


class AuthApi:

    @staticmethod
    def login(payload):
        return ApiClient.post(
            REQRES_BASE_URL,
            "/app-users/login",
            payload
        )

    @staticmethod
    def verify(payload):
        return ApiClient.post(
            REQRES_BASE_URL,
            "/app-users/verify",
            payload
        )