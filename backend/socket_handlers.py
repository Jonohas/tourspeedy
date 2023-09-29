import socketio
from classes.TimingClass import TimingClass

tc = TimingClass()


sio_server = socketio.AsyncServer(
    async_mode='asgi',
    cors_allowed_origins=[]
)

sio_app = socketio.ASGIApp(
    socketio_server=sio_server,
    socketio_path='socket.io'
)


@sio_server.event
async def connect(sid, environ, auth):
    print(f'{sid}: connected')
    await sio_server.emit('join', {'sid': sid})

@sio_server.event
async def disconnect(sid):
    print(f'{sid}: disconnected')

@sio_server.event
async def ready(sid):
    print(f'{sid}: ready')
    tc.ready = True
    await sio_server.emit('ready', {'sid': sid})
