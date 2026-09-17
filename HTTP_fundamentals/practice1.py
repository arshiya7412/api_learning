import requests

response = requests.get("https://jsonplaceholder.typicode.com/users/1")
print(response.request.method)
print(response.status_code)
json = response.headers
json1 = response.json()
print(json['Content-Type'])
print(json1['name'])