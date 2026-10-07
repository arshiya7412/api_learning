#pydantic model
from fastapi import FastAPI
from pydantic import BaseModel

class Student(BaseModel):
    name: str
    age: int
    dept: str

app = FastAPI()
@app.post("/students")
def post_student(student: Student):
    return student