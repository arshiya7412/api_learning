import requests
user_id = 5
response = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
print(response.status_code)
data = response.json()
print(data['name'])
print(data['email'])