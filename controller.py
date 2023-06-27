import uvicorn
import json
from fastapi import FastAPI
from fastapi import Request
from fastapi.middleware.cors import CORSMiddleware

APP_PATH = '/usr/share/nginx/html/data/'
#APP_PATH = "/Volumes/Data/localsites/masterliveaboards.com/"
app = FastAPI()

origins = [
    "http://localhost:9001",
    "https://guests.masterliveaboards.com"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/answers")
async def saveAnswers(request: Request):

    requestDic = await request.json()

    jsonDataDump = json.dumps(requestDic)

    destination = APP_PATH + requestDic['id'] + ".json"

    with open(destination, "w") as outfile:
        outfile.write(jsonDataDump)

@app.get("/answers")
async def saveAnswers(request: Request):


    requestDic = await request.json()

    jsonDataDump = json.dumps(requestDic)

    destination = APP_PATH + requestDic['id'] + ".json"

    with open(destination, "w") as outfile:
        outfile.write(jsonDataDump)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)