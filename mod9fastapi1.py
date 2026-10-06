from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "welcome to my API"}

@app.get("/about")
def about():
    return{
    "name": "Arshiya",
    "field": "AI & Data Science"
}

@app.get("/status")
def status():
    return{
    "status": "API is running"
}