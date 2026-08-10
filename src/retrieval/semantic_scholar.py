import requests
from dotenv import load_dotenv
import os
import time

load_dotenv()

API_KEY = os.getenv("SEMANTIC_SCHOLAR_API_KEY")

SEARCH_URL = "https://api.semanticscholar.org/graph/v1/paper/search"

def search_papers(query, limit=5):
    params = {
        "query": query,
        "fields": "paperId,title,abstract,year",
        "limit": limit,
    }

    headers = {"x-api-key": API_KEY}

    response = requests.get(
        SEARCH_URL,
        params=params,
        headers=headers
    )

    if response.status_code == 429:
      time.sleep(2)
      response = requests.get(
        SEARCH_URL,
        params=params,
        headers=headers
      )

    response.raise_for_status()

    return response.json()