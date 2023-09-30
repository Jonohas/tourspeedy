from classes.SensorWatcher import SensorWatcher
from classes.Singleton import Singleton
from socket_handlers import SocketIOServer


class TimingClass(metaclass=Singleton):
    def __init__(self):
        # Check if the object already has the attribute 'value'
        # If it doesn't, it means it's a newly created object
        if not hasattr(self, '_timestamp1'):
            self._timestamp1 = None
            self._timestamp2 = None
            self._ready = False
            self.sensor_watcher_thread = None  # To hold the reference of ButtonWatcher thread.
            self.sio = SocketIOServer(self).sio

    @property
    def ready(self):
        return self._ready

    @ready.setter
    def ready(self, value):
        self._ready = value

        if value:
            if not self.sensor_watcher_thread:
                self.start_thread()

        elif self.sensor_watcher_thread:
            self.sensor_watcher_thread.stop_event.set()  # Signal the thread to stop.
            self.sensor_watcher_thread.join()  # Wait for the thread to finish.
            self.sensor_watcher_thread = None  # Clear the reference to the thread.

    @property
    def timestamp1(self):
        return self._timestamp1

    @timestamp1.setter
    def timestamp1(self, value):
        self._timestamp1 = value

    @property
    def timestamp2(self):
        return self._timestamp2

    @timestamp2.setter
    def timestamp2(self, value):
        self._timestamp2 = value

    def start_thread(self):
        self.sensor_watcher_thread = SensorWatcher(self)  # Create the thread with a reference to this instance.
        self.sensor_watcher_thread.start()  # Start the thread.


        
