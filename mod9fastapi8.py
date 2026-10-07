from fastapi import FastAPI, status
app = FastAPI()
@app.post("/product", status_code=status.HTTP_201_CREATED)
def create_product ():
    return {"message": "product created"}