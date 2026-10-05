# response body
import requests
data_1 = {
    "title": "Learning APIs",
    "body": "I'm Learning HTTP request & responses",
    "userId": 3
    }
response = requests.post("https://jsonplaceholder.typicode.com/posts", json=data_1)
print(response.status_code)
data = response.json()
print(data['userId'])
print(data['title'])
print(data['id'])