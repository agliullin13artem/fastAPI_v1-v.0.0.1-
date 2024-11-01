from fastapi import FastAPI


import uvicorn

from items_views import router as items_router
from users.views import router as users_router


app = FastAPI()
app.include_router(items_router)
app.include_router(users_router)





@app.get("/")
def hello_world():
    return {"message": "Hello, World!"}


@app.get("/hello/")
def hello_world(name: str = "ARtem"):
    name = name.strip().lower()
    return {"message": f"Hello, World! {name}"}


@app.get("/calc/add/")
def add(a: int, b: int):
    return {"a": a, "b": b, "result": a + b}


# для запуска
if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
