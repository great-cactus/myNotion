import os
from notion_client import Client, APIErrorCode, APIResponseError
from pprint import pprint
import logging

NOTION_TOKEN = os.environ["NOTION_TOKEN"]
#DATABASE_ID = os.environ["DATABASE_ID"]
DATABASE_ID = os.environ["GTD_TASK_ID"]
notion = Client(auth=NOTION_TOKEN)
list_users_response = notion.users.list()
#pprint(list_users_response)

try:
    my_page = notion.databases.query(
            **{
                "database_id": DATABASE_ID
                }
            )
except APIResponseError as error:
    if error.code == APIErrorCode.ObjectNotFound:
        print("Database not found error, bye!")
    else:
        print("Yokuwakannnai error")
        logging.error(error)

#pprint(my_page)

notion.pages.create( # add data to the database
        **{
            "parent": { "database_id": DATABASE_ID}, # Specify your database ID
            "properties": {
                "名前": {
                    "title": [ { "text": {"content": "API TEST"} } ]
                    }
                }
            }
        )
