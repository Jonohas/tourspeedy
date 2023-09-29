import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from classes.TimingClass import TimingClass
from socket_handlers import SocketIOServer

app = FastAPI()

sio_app = SocketIOServer().app
app.mount('/', app=sio_app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
async def home():
    return {'message': 'Hello👋 Developers💻'}



if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
