from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()

@app.post("/createposts")

def create_posts(payLoad: dict = Body(...)):
    print(payLoad)
    return {"message":"successfully created posts"}
