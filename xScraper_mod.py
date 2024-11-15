import csv
import pandas as pd
import tweepy
import os
import urllib.parse
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Retrieve Twitter API credentials from environment variables
api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")
bearer_token = os.getenv("BEARER_TOKEN")

# Initialize the Twitter API client
client = tweepy.Client(
    consumer_key=api_key,
    consumer_secret=api_secret,
    access_token=access_token,
    access_token_secret=access_token_secret,
    bearer_token=bearer_token,
    wait_on_rate_limit=True
)

def read_csv(filepath="./datafile/twitter_links.xlsx"):
    """
    Read an Excel file containing Twitter links and return a list of links.

    :param filepath: Path to the Excel file.
    :return: List of Twitter links.
    """
    data = pd.read_excel(filepath)
    return data["Links"].tolist()

def get_username(link):
    """
    Extract the username from a Twitter link.

    :param link: Twitter profile link.
    :return: Username extracted from the link.
    """
    return urllib.parse.urlparse(link).path.strip('/')

def get_user_data(username):
    """
    Retrieve user data from Twitter API.

    :param username: Twitter username.
    :return: User data.
    """
    user = client.get_user(username=username, user_fields=["description", "public_metrics", "location", "url"])
    return user

def extract_information(user):
    """
    Extract relevant information from user data.

    :param user: User data from Twitter API.
    :return: List of dictionaries containing user information.
    """
    user_data = []
    user_info = {
        "Bio": user.data.description,
        "Following Count": user.data.public_metrics["following_count"],
        "Followers Count": user.data.public_metrics["followers_count"],
        "Location": user.data.location,
        "Website": user.data.url
    }
    user_data.append(user_info)
    return user_data

def write_to_csv(data, filename="users_data.csv", mode='a', write_header=False):
    """
    Append user information to a CSV file.

    :param data: List of dictionaries containing user information.
    :param filename: Name of the CSV file.
    :param mode: File mode, default is 'a' for append.
    :param write_header: Boolean indicating whether to write the header.
    """
    fieldnames = ["Bio", "Following Count", "Followers Count", "Location", "Website"]
    with open(filename, mode=mode, newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if write_header:
            writer.writeheader()
        writer.writerows(data)
    print(f"{filename} has been updated successfully!")


def main():
    """
    Main function to execute the data extraction and writing process.
    """
    links = read_csv()
    all_user_data = []  # Initialize an empty list to hold all user data
    header_written = False  # Track if header is written

    for link in links:
        username = get_username(link)
        user = get_user_data(username)
        user_data = extract_information(user)

        # If header hasn't been written yet, write it along with the first batch of data
        if not header_written:
            write_to_csv(user_data, mode='w', write_header=True)
            header_written = True
        else:
            write_to_csv(user_data)

if __name__ == "__main__":
    main()
