#API keys
import requests

headers = {
    "X-API-Keys": "my-secret-key-123"
}
response = requests.get("https://example.com/weather", headers=headers)
print(response.status_code)