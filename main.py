# Import the requests package so Python can communicate with Semantic Scholar.
import requests

# Store the Semantic Scholar paper-search endpoint.
url = "https://api.semanticscholar.org/graph/v1/paper/search"

# Store the information we want to send to Semantic Scholar.
params = {
    # Tell Semantic Scholar what topic we want to search for.
    "query": "federated learning",

    # Ask Semantic Scholar to return these four pieces of information.
    "fields": "paperId,title,abstract,year",

    # Ask for only 5 papers for our first test.
    "limit": 5
}

# Send a GET request to Semantic Scholar with our search information.
response = requests.get(url, params=params)

# Print the HTTP status code returned by Semantic Scholar.
print("Status code:", response.status_code)

# Convert the JSON response into Python data.
data = response.json()

# Print the complete response so we can inspect what Semantic Scholar returned.
print(data)