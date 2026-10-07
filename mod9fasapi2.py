from fastapi import FastAPI

app = FastAPI()
@app.get("/students")
def get_students():
    return {"message": "getting student"}

@app.get("/students/1")
def get_students_1():
    return {"student_id": 1}

@app.post("/students")
def create_students():
    return {
        "name": "Arshiya",
        "Class": 6,
        "Section": "A"
    }

@app.put("/students/1")
def update_students():
    return {"students_id": 3}

@app.delete("/students/1")
def delete_students():
    return 0