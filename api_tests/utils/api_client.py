import requests


class ApiClient:

    BASE_URL = "https://jsonplaceholder.typicode.com"

    @staticmethod
    def get(endpoint):
        return requests.get(f"{ApiClient.BASE_URL}{endpoint}")

    @staticmethod
    def post(endpoint, payload):
        return requests.post(f"{ApiClient.BASE_URL}{endpoint}", json=payload)