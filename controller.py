import uvicorn
from fastapi import FastAPI
from fastapi import Request
from fastapi.middleware.cors import CORSMiddleware

APP_PATH = '/usr/share/nginx/html/data/'
#PP_PATH = '/Volumes/Data/localsites/masterliveaboards.com/'
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


    json = await request.json()


    destination = APP_PATH + json.guest_id + ".json"

    with open(destination, "w") as outfile:
        outfile.write(json)

@app.get("/answers")
async def saveAnswers(request: Request):

    json = await request.json()

    destination = APP_PATH + json.guest_id + ".json"

    with open(destination, "w") as outfile:
        outfile.write(json)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)