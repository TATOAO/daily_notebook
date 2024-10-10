from fastapi import FastAPI

app = FastAPI()


@app.get("/hello")
async def root():
    return {"message": "Hello World"}


# fastapi dev hello_world.py
