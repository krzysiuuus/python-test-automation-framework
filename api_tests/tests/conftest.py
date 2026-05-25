import pytest
from api_tests.utils.data_generator import DataGenerator


@pytest.fixture
def create_post_payload():
    return DataGenerator.generate_post_payload()