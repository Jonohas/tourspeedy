import socketio
from classes.Singleton import Singleton



class SocketIOServer(metaclass=Singleton):
    def __init__(self, tc):
        if not hasattr(self, 'sio'):

            self._tc = tc
            self.sio = socketio.AsyncServer(
                async_mode='asgi',
                cors_allowed_origins=[]
            )
            self.app = socketio.ASGIApp(
                socketio_server=self.sio,
                socketio_path='sockets'
            )

            @self.sio.event
            async def connect(sid, environ, auth):
                print(f'{sid}: connected')
                await self.sio.emit('join', {'sid': sid})

            @self.sio.event
            async def disconnect(sid):
                print(f'{sid}: disconnected')

            @self.sio.event
            async def ready(sid):
                print(f'{sid}: ready')
                if self._tc:
                    self._tc.ready = True
                else:
                    print("tc not ready yet")
                await self.sio.emit('ready', {'sid': sid})




