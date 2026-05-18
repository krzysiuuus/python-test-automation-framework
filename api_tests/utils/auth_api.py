from api_tests.utils.api_client import ApiClient


class AuthApi:

    BASE_URL = "https://reqres.in/api"

    @staticmethod
    def login(payload):
        return ApiClient.post(AuthApi.BASE_URL, "/login", payload)