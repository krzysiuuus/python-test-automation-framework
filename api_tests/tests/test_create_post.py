import allure

from api_tests.utils.posts_api import PostsApi


@allure.feature("Posts API")
@allure.story("Create new post")
class TestCreatePost:

    @allure.title("Verify new post can be created")
    def test_create_post(self, create_post_payload):
        response = PostsApi.create_post(create_post_payload)

        assert response.status_code == 201

        response_body = response.json()

        assert response_body["title"] == create_post_payload["title"]
        assert response_body["body"] == create_post_payload["body"]
        assert response_body["userId"] == create_post_payload["userId"]