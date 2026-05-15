import allure

from api_tests.utils.posts_api import PostsApi
from api_tests.data.create_post_payload import CREATE_POST_PAYLOAD


@allure.feature("Posts API")
@allure.story("Create new post")
class TestCreatePost:

    @allure.title("Verify new post can be created")
    def test_create_post(self):

        payload = CREATE_POST_PAYLOAD

        response = PostsApi.create_post(payload)

        assert response.status_code == 201

        response_body = response.json()

        assert response_body["title"] == payload["title"]
        assert response_body["body"] == payload["body"]
        assert response_body["userId"] == payload["userId"]