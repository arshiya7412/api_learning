#Headers
import requests
response = requests.get("https://jsonplaceholder.typicode.com/posts/3")
print(response.status_code)
print(response.headers["Content-Type"])