import requests

from config.config import REQRES_API_KEY
from utils.logger import get_logger

logger = get_logger(__name__)

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
        logger.info(f"GET {base_url}{endpoint}")

        response = ApiClient.session.get(f"{base_url}{endpoint}")

        logger.info(f"Response status code: {response.status_code}")

        return response

    @staticmethod
    def post(base_url, endpoint, payload):
        logger.info(f"POST {base_url}{endpoint}")
        logger.info(f"Request payload: {payload}")

        response = ApiClient.session.post(f"{base_url}{endpoint}", json=payload)

        logger.info(f"Response status code: {response.status_code}")

        return response

    @staticmethod
    def put(base_url, endpoint, payload):
        logger.info(f"PUT {base_url}{endpoint}")
        logger.info(f"Request payload: {payload}")

        response = ApiClient.session.put(f"{base_url}{endpoint}", json=payload)

        logger.info(f"Response status code: {response.status_code}")

        return response

    @staticmethod
    def delete(base_url, endpoint):
        logger.info(f"DELETE {base_url}{endpoint}")

        response = ApiClient.session.delete(f"{base_url}{endpoint}")

        logger.info(f"Response status code: {response.status_code}")

        return response