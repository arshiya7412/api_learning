import requests

response = requests.get("https://jsonplaceholder.typicode.com/users/1")
print(response.status_code)
data = response.json()
print(data["name"])
print(data["username"])

#create a fake user
data_1 = {
          "name": "Arshiya",
          "username": "arshiya7412"
          }
response = requests.post("https://jsonplaceholder.typicode.com/users/", json=data_1)
print(response.status_code)
mod_data = response.json()
print(mod_data["name"])
print(mod_data["username"])

#update user
response = requests.put("https://jsonplaceholder.typicode.com/users/1", json=data_1)
print(response.status_code)
update_data = response.json()
print(update_data["name"])
print(update_data["username"])

#delete user
response = requests.delete("https://jsonplaceholder.typicode.com/users/1", json=data_1)
print(response.status_code)

#add header to request

header = {
    "Content-Type": "application/json"
         }
response = requests.post("https://jsonplaceholder.typicode.com/users/", json=data_1, headers=header)
print(response.status_code)