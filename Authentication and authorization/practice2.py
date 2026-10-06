# bearer tokens 
import requests

headers = {
    "Authorization": "Bearer my-access-token-123"
}
response = requests.get("https://example.com/profile", headers=headers)
print(response.status_code)