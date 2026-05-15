import allure

from api_tests.data.update_post_payload import UPDATE_POST_PAYLOAD
from api_tests.utils.posts_api import PostsApi


@allure.feature("Posts API")
@allure.story("Update post")
class TestUpdatePost:

    @allure.title("Verify post can be updated")
    def test_update_post(self):

        response = PostsApi.update_post(1, UPDATE_POST_PAYLOAD)

        assert response.status_code == 200
        assert response.elapsed.total_seconds() < 2

        response_body = response.json()

        assert response_body["title"] == "updated title"
        assert response_body["body"] == "updated body"