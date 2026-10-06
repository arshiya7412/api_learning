#API keys
import os
from dotenv import load_dotenv
import requests

load_dotenv()

token = os.getenv("API_KEY")

headers = {
    "X-API-KEY": f"{token}"
}
response = requests.get("https://example.com/weather", headers=headers)
print(response.status_code)