#response body
import requests
response = requests.get("https://jsonplaceholder.typicode.com/posts/3")
print(response.status_code)
data = response.json()
print(data['id'])
print(data['title'])
print(data['userId'])