#query parameter
from fastapi import FastAPI
app = FastAPI()
@app.get("/product/")
def get_category(category: str):
    return {"category": category} 