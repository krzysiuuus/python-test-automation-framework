from api_tests.utils.api_client import ApiClient


class PostsApi:

    @staticmethod
    def get_posts():
        return ApiClient.get("/posts")

    @staticmethod
    def create_post(payload):
        return ApiClient.post("/posts", payload)

    @staticmethod
    def update_post(post_id, payload):
        return ApiClient.put(f"/posts/{post_id}", payload)

    @staticmethod
    def delete_post(post_id):
        return ApiClient.delete(f"/posts/{post_id}")