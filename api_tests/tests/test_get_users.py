import allure
from api_tests.utils.posts_api import PostsApi


@allure.feature("Posts API")
@allure.story("Get posts list")
class TestGetUsers:

    @allure.title("Verify posts list can be downloaded")
    def test_get_users(self):
        response = PostsApi.get_posts()

        assert response.status_code == 200
        assert response.elapsed.total_seconds() < 2

        response_body = response.json()

        assert len(response_body) > 0
        assert response_body[0]["userId"] == 1