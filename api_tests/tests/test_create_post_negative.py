import allure
from api_tests.utils.posts_api import PostsApi


@allure.feature("Posts API")
@allure.story("Create invalid post")
class TestCreateInvalidPost:

    @allure.title("Verify invalid payload handling")
    def test_create_invalid_post(self):

        payload = {}

        response = PostsApi.create_post(payload)

        assert response.status_code == 201
        assert response.elapsed.total_seconds() < 2

        response_body = response.json()

        assert "id" in response_body