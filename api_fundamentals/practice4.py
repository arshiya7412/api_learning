import requests

response = requests.post("https://jsonplaceholder.typicode.com/users/", json={"username": "arshiya7412", "name": "Arshiya"})
print(response)
print(response.status_code)
data = response.json()
print(data)
print(data["username"])
print(data["name"])