from api_tests.utils.api_client import ApiClient
from config.config import API_BASE_URL


class PostsApi:

    BASE_URL = API_BASE_URL

    @staticmethod
    def get_posts():
        return ApiClient.get(PostsApi.BASE_URL, "/posts")

    @staticmethod
    def create_post(payload):
        return ApiClient.post(PostsApi.BASE_URL, "/posts", payload)

    @staticmethod
    def update_post(post_id, payload):
        return ApiClient.put(PostsApi.BASE_URL, f"/posts/{post_id}", payload)

    @staticmethod
    def delete_post(post_id):
        return ApiClient.delete(PostsApi.BASE_URL, f"/posts/{post_id}")