import allure
import requests


@allure.feature("Posts API")
@allure.story("Get posts list")
class TestGetPosts:

    @allure.title("Verify posts list can be downloaded")
    def test_get_posts(self):
        response = requests.get("https://jsonplaceholder.typicode.com/posts")

        assert response.status_code == 200

        response_body = response.json()

        assert len(response_body) > 0
        assert response_body[0]["userId"] == 1