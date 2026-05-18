import pytest


@pytest.fixture
def create_post_payload():
    return {
        "title": "My post",
        "body": "Hello world",
        "userId": 1
    }