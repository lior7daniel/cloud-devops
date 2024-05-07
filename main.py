from src.aws.handlers import IAMHandler


def main():
    # Instantiate IAMHandler
    iam_handler = IAMHandler()
    iam_users = iam_handler.fetch_data()

    # Process IAM users data or perform other operations


if __name__ == "__main__":
    main()
