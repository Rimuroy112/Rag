from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

class post(BaseModel):
    title: str
    content: str
    published: bool=True
    rating: Optional[int] = None

@app.post("/createposts")

def create_posts(new_post: post):
    print(new_post.published)
    print(new_post.rating)
    print(new_post.dict())
    return{"data": "new_post"}

