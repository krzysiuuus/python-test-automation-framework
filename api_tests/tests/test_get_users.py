import allure
from api_tests.utils.users_api import UsersApi


@allure.feature("Users API")
@allure.story("Get users list")
class TestGetUsers:

    @allure.title("Verify users list can be downloaded")
    def test_get_users(self):
        response = UsersApi.get_users()

        assert response.status_code == 200
        assert response.elapsed.total_seconds() < 2

        response_body = response.json()

        assert len(response_body) > 0
        assert response_body[0]["id"] == 1