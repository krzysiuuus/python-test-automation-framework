import allure

from api_tests.utils.posts_api import PostsApi


@allure.feature("Posts API")
@allure.story("Delete post")
class TestDeletePost:

    @allure.title("Verify post can be deleted")
    def test_delete_post(self):

        response = PostsApi.delete_post(1)

        assert response.status_code == 200
        assert response.elapsed.total_seconds() < 2