from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World,Welcome to my API.I Like AI"}

@app.get("/posts")
def get_posts():
    return {"data":"This is your posts"}
