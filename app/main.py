import sys
import random

from fastapi import FastAPI

version = f"{sys.version_info.major}.{sys.version_info.minor}"

app = FastAPI()

@app.get("/")
async def read_root():
    message = f"Hello world! From FastAPI running on Uvicorn with Gunicorn. Using Python {version} while openshift is doing its thing"
    return {"message": message}


@app.get("/concurrency")
async def test_concurrency():
    range_for_request = random.randrange(20, 2000)
    items = []
    for i in range(2, range_for_request):
        if (range_for_request % i) == 0:
            items.append(i)

    return {"message": items}

@app.get("/testing")
def testing():
    range_for_request = random.randrange(20, 2000)
    items = []
    for i in range(2, range_for_request):
        if (range_for_request % i) == 0:
            items.append(i)

    return {"message": items}
