import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

CONFLUENCE_EMAIL = os.getenv("CONFLUENCE_EMAIL")
CONFLUENCE_API_TOKEN = os.getenv("CONFLUENCE_API_TOKEN")
BASE_URL = os.getenv("CONFLUENCE_BASE_URL")      # e.g. https://juz40.atlassian.net/wiki
SPACE_KEY = os.getenv("CONFLUENCE_SPACE_KEY")    # e.g. QA
PARENT_PAGE_ID = os.getenv("CONFLUENCE_PARENT_ID")  # ID of folder "Test Cases"


def create_confluence_page(title, html):
    url = f"{BASE_URL}/rest/api/content"

    body = {
        "type": "page",
        "title": title,
        "ancestors": [{"id": PARENT_PAGE_ID}],
        "space": {"key": SPACE_KEY},
        "body": {
            "storage": {
                "value": html,
                "representation": "storage"
            }
        }
    }

    response = requests.post(
        url,
        auth=(CONFLUENCE_EMAIL, CONFLUENCE_API_TOKEN),
        headers={"Content-Type": "application/json"},
        data=json.dumps(body)
    )

    r = response.json()

    return BASE_URL + r["_links"]["webui"]
