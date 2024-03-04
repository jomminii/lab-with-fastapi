from fastapi import FastAPI

from app.test.src import three_eventloop

app = FastAPI()

@app.get("/")
async def root():

    return {"message": "Hello World"}

@app.get("/03_eventloop/{idx}")
async def eventloop(
    idx: int,
):
    three_eventloop.test_eventloop_sync(idx)
    # await three_eventloop.test_eventloop_async(idx)
    return {"message": "Hello World"}