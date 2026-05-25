from faker import Faker

fake = Faker()


class DataGenerator:

    @staticmethod
    def generate_post_payload():
        return {
            "title": fake.sentence(),
            "body": fake.text(),
            "userId": fake.random_int(min=1, max=10)
        }

    @staticmethod
    def generate_invalid_post_payload():
        return {
            "title": "",
            "body": "",
            "userId": "invalid"
        }