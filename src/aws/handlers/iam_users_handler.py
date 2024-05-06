import boto3
import logging

from src.aws.handlers.base_handler import BaseHandler

logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


class IAMHandler(BaseHandler):
    def fetch_data(self):
        try:
            # Create a Boto3 client with the IAM service
            iam_client = boto3.client('iam')

            # List users
            response = iam_client.list_users()
            users = response['Users']

            # Log success message
            logger.info("Successfully fetched users from AWS IAM")

            # Process user data or return it if needed
            return users

        except Exception as e:
            logger.error(f"Error occurred: {str(e)}")
            return None
