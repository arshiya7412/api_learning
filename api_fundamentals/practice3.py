import requests

response = requests.get("https://jsonplaceholder.typicode.com/users/1", timeout = 10)
print(response.status_code)
data = response.json()
print(data)
print(data['id'])
print(data['name'])
print(data['username'])