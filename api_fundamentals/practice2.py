import requests

response = requests.get(response = requests.get("https://jsonplaceholder.typicode.com/users/1"), params = {"username": "Bret"})
print(response)
data = response.json()
print(data[0]['name'])