from api_tests.utils.api_client import ApiClient


class PostsApi:

    @staticmethod
    def get_posts():
        return ApiClient.get("/posts")

    @staticmethod
    def create_post(payload):
        return ApiClient.post("/posts", payload)