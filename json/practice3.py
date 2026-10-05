import json

user = {
    "name": "Alex",
    "age": 20,
    "skills": [
        "Python", "html", "sql"
    ]
}
json_sdata = json.dumps(user)
print(json_sdata)
data = json.loads(json_sdata)
print(data)
print(data['name'])
