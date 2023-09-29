import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from socket_handlers import sio_app
from classes.TimingClass import TimingClass

app = FastAPI()
app.mount('/', app=sio_app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

tc = TimingClass()

@app.get('/')
async def home():
    return {'message': 'Hello👋 Developers💻'}



if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
