# bearer tokens 
import os
from dotenv import load_dotenv
import requests

load_dotenv()
token = os.getenv("API_KEY")
headers = {
    "Authorization": f"Bearer {token}"
}
response = requests.get("https://example.com/profile", headers=headers)
print(response.status_code)