import socketio
from classes.Singleton import Singleton
from classes.DB import add_event, get_all_events, event_to_dict, events_to_json
import datetime
from classes.Lights import Lights
import RPi.GPIO as GPIO


class SocketIOServer(metaclass=Singleton):
    def __init__(self, tc):
        if not hasattr(self, 'sio'):

            self._tc = tc
            self._lights = Lights()
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
                await self.sio.emit('join', {'sid': sid})
                events = get_all_events()
                events_list = [event_to_dict(event) for event in events]
                self._lights.handle_lights([GPIO.LOW, GPIO.LOW, GPIO.LOW, GPIO.HIGH])
                await self.sio.emit("events", {"events": events_list})

            @self.sio.event
            async def disconnect(sid):
                pass

            @self.sio.event
            async def ready(sid):
                if self._tc:
                    self._tc.ready = True
                else:
                    print("tc not ready yet")

                self._lights.handle_lights([GPIO.HIGH, GPIO.LOW, GPIO.LOW, GPIO.LOW])
                await self.sio.emit('ready', {'ready': True})

            @self.sio.event
            async def save(sid, data):
                add_event(int(data["startnumber"]), data["license_plate"], datetime.datetime.fromtimestamp(data["start"]), datetime.datetime.fromtimestamp(data["stop"]), int(data["distance"]), int(data["speed"]), data["session_name"])
                events = get_all_events()
                events_list = [event_to_dict(event) for event in events]
                await self.sio.emit('save', {})







