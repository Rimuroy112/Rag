from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

class post(BaseModel):
    title: str
    content: str

@app.post("/createposts")

def create_posts(new_post: post):
    print(new_post)
    return{"data": "new_post"}

