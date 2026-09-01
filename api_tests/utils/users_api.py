from api_tests.utils.api_client import ApiClient
from core.config import API_BASE_URL


class UsersApi:
    """Responsible for user endpoints"""

    BASE_URL = API_BASE_URL

    @staticmethod
    def get_users():
        return ApiClient.get(UsersApi.BASE_URL, "/users")

    @staticmethod
    def get_user(user_id):
        return ApiClient.get(UsersApi.BASE_URL, f"/users/{user_id}")