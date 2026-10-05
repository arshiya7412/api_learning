#Error response
import requests
response = requests.get("https://jsonplaceholder.typicode.com/posts/99999")
print(response.status_code)

if response.status_code == 200:
    data = response.json()
    print(data)
    print(data['title'])
else:
    print("Error", response.status_code)