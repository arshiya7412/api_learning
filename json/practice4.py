import json

user = {
    "name": "Arshiya",
    "age": 20,
    "is_student": True,
    "skills": ["python", "C", "C++"],
    "Address": {
        "City": "Chennai",
        "Country": "India"
    }
}

json_data = json.dumps(user)
print(json_data)
data = json.loads(json_data)
print(data)
print(data['name'])
print(data['is_student'])
print(data['skills'][0])
print(data['Address']['City'])
print(type(data['skills']))
print(type(data['age']))
print(type(data['is_student']))