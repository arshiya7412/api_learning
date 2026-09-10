import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")
print(response)
print(response.headers)
print(response.status_code)
names = response.json()
for na_me in names:
    print(na_me['name'])
response = requests.get("https://jsonplaceholder.typicode.com/users", params = {"username": "Bret"})
print(response)
data = response.json()
print(data[0]['name'])