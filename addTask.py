import os
from notion_client import Client, APIErrorCode, APIResponseError
import logging
import sys

# Get Notion API token and database ID from environment variables
NOTION_TOKEN = os.environ["NOTION_TOKEN"]
DATABASE_ID = os.environ["GTD_TASK_ID"]

# Initialize Notion client
notion = Client(auth=NOTION_TOKEN)
# Retrieve a list of users
list_users_response = notion.users.list()

try:
    # Query the database to retrieve data
    my_page = notion.databases.query(
        **{
            "database_id": DATABASE_ID
        }
    )
except APIResponseError as error:
    if error.code == APIErrorCode.ObjectNotFound:
        print("Database not found error, bye!")
    else:
        print("Unknown error occurred")
        logging.error(error)

# Get input from command-line argument
addTXT = sys.argv[1:]
addTXT = ' '.join(addTXT)

# Create a new page and add data to the database
notion.pages.create(
    **{
        "parent": {"database_id": DATABASE_ID},  # Specify your database ID
        "properties": {
            "名前": {
                "title": [{"text": {"content": addTXT}}]
            }
        }
    }
)
