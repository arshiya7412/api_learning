#request body
from fastapi import FastAPI, Body
app = FastAPI()

@app.post("/students")
def students(student: dict=Body({
    "name": "Arshiya",
    "age": 21,
    "department": "AI & DS"
})):
    return student