from classes.SensorWatcher import SensorWatcher
from classes.Singleton import Singleton

    

class TimingClass(metaclass=Singleton):
    def __init__(self):
        # Check if the object already has the attribute 'value'
        # If it doesn't, it means it's a newly created object
        if not hasattr(self, '_timestamp1'):
            self._timestamp1 = None
            self._timestamp2 = None

            self._ready = False
            self.sensor_watcher_thread = None  # To hold the reference of ButtonWatcher thread.

    @property
    def ready(self):
        return self._ready

    @ready.setter
    def ready(self, value):
        self._ready = value

        if value:
            self.sensor_watcher_thread = SensorWatcher(self)  # Create the thread with a reference to this instance.
            self.sensor_watcher_thread.start()  # Start the thread.
        elif self.sensor_watcher_thread:
            self.sensor_watcher_thread.stop_event.set()  # Signal the thread to stop.
            self.sensor_watcher_thread.join()  # Wait for the thread to finish.
            self.sensor_watcher_thread = None  # Clear the reference to the thread.


        
