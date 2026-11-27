from fastapi import FastAPI
from fastapi.responses import HTMLResponse
app = FastAPI()

posts: list[dict] = [
    {
        "id": 1,
        "author": "Tanish",
        "title": "FastAPI is Awesome",
        "content": "This framework is really easy to use and super fast.",
        "date_posted": "April 20, 2025",
    },
    {
        "id": 2,
        "author": "Jane Doe",
        "title": "Python is Great for Web Development",
        "content": "Python is a great language for web development, and FastAPI makes it even better.",
        "date_posted": "April 21, 2025",
    },
]

@app.get("/", response_class=HTMLResponse, include_in_schema=False) # returns the HTML data of the home page.)
@app.get("/posts", response_class=HTMLResponse,include_in_schema=False)
def home():
    return F"<h1>{posts[0]['author']}</h1/>"

@app.get("/api/posts") # returns the JSON data of the posts. 
def get_posts():
    return posts 