import allure
from api_tests.utils.api_client import ApiClient


@allure.feature("Users API")
@allure.story("Get non existing user")
class TestUserNotFound:

    @allure.title("Verify API returns 404 for non existing user")
    def test_user_not_found(self):

        response = ApiClient.get("/users/999999")

        assert response.status_code == 404
        assert response.elapsed.total_seconds() < 2