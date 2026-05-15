import allure
import pytest

from api_tests.utils.api_client import ApiClient
from jsonschema import validate
from api_tests.schemas.user_schema import USER_SCHEMA


@allure.feature("Users API")
@allure.story("Get single user")
class TestGetSingleUser:

    @pytest.mark.parametrize("user_id", [1, 2, 3])
    @allure.title("Verify single user can be downloaded")
    def test_get_single_user(self, user_id):

        response = ApiClient.get(f"/users/{user_id}")

        assert response.status_code == 200
        assert response.elapsed.total_seconds() < 2

        response_body = response.json()

        assert response_body["id"] == user_id

        validate(instance=response_body, schema=USER_SCHEMA)