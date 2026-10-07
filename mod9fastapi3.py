#path parameter
from fastapi import FastAPI
app = FastAPI()
@app.get("/student/{student_id}")
def get_student_id(student_id: int):
    return {"student_id": student_id}