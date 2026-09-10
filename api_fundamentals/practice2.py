import requests

response = requests.get("https://jsonplaceholder.typicode.com/users", params = {"username": "Bret"})
print(response)
data = response.json()
print(data[0]['name'])