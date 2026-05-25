import requests

from config.config import REQRES_API_KEY


class ApiClient:

    session = requests.Session()

    session.headers.update({
        "Content-Type": "application/json",
        "Accept": "application/json",
        "x-api-key": REQRES_API_KEY
    })

    @staticmethod
    def set_token(token):
        ApiClient.session.headers.update({
            "Authorization": f"Bearer {token}"
        })

    @staticmethod
    def get(base_url, endpoint):
        return ApiClient.session.get(f"{base_url}{endpoint}")

    @staticmethod
    def post(base_url, endpoint, payload):
        return ApiClient.session.post(f"{base_url}{endpoint}", json=payload)

    @staticmethod
    def put(base_url, endpoint, payload):
        return ApiClient.session.put(f"{base_url}{endpoint}", json=payload)

    @staticmethod
    def delete(base_url, endpoint):
        return ApiClient.session.delete(f"{base_url}{endpoint}")