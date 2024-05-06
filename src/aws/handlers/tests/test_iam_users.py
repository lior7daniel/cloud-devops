import unittest
from unittest.mock import MagicMock

from src.aws.handlers.iam_users_handler import IAMHandler


class TestIAMHandler(unittest.TestCase):
    def test_fetch_data(self):
        # Mock the behavior of the boto3 client
        boto3_client_mock = MagicMock()
        boto3_client_mock.list_users.return_value = {'Users': [{'UserName': 'test_user', 'UserId': '123'}]}

        # Patch the boto3.client method to return the mock
        with unittest.mock.patch('boto3.client', return_value=boto3_client_mock):
            # Instantiate IAMHandler
            iam_handler = IAMHandler()

            # Fetch data
            iam_users = iam_handler.fetch_data()

            # Assert that the result is not None
            self.assertIsNotNone(iam_users, "Failed to fetch data from AWS IAM")
