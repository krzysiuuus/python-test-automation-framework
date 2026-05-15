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

        response_body = response.json()

        assert response_body == {}