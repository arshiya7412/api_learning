from pydantic import BaseModel
from fastapi import FastAPI

class Student(BaseModel):
    name: str
    age: int
    dept: str

app = FastAPI()
@app.get("/student", response_model=Student)
def student():
    return {
        "name": "Arshiya",
        "age": 20,
        "dept": "AIDS"
    }