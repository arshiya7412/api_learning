import requests
params = {
    "userId": 3
}
response = requests.get("https://jsonplaceholder.typicode.com/posts", params=params)

print(response.status_code)
data = response.json()

print(data[0]['title'])