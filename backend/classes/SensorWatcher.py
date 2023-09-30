import threading
import time
import asyncio


from classes.Singleton import Singleton
from classes.ButtonGrid import ButtonGrid


class SensorWatcher(threading.Thread):
    def __init__(self, timing_instance):
        super(SensorWatcher, self).__init__()
        self.bg = ButtonGrid()


        self.timing_instance = timing_instance
        self.lock = threading.Lock()
        self.stop_event = threading.Event()  # Event to signal the thread to stop.


    def run(self):
        print("Start Sync Function")
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self.start_sensor_watch())
        print("End Sync Function")

    async def start_sensor_watch(self):
        self.timing_instance.ready = True
        print("Starting SensorWatcher Thread...")
        try:
            while not self.stop_event.is_set():  # Check if the thread is signaled to stop.
                response = self.bg.scan()
                if not response[0][0]:
                    with self.lock:
                        if not self.timing_instance.timestamp1:
                            self.timing_instance.timestamp1 = time.time()
                            print("Start")
                            await self.timing_instance.sio.emit('start', {'timestamp': self.timing_instance.timestamp1})

                if not response[0][1]:
                    with self.lock:
                        if not self.timing_instance.timestamp2 and self.timing_instance.timestamp1:
                            self.timing_instance.timestamp2 = time.time()
                            print("Stop:", (self.timing_instance.timestamp2 - self.timing_instance.timestamp1) * 1000, "milliseconds")
                            await self.timing_instance.sio.emit('stop', {'timestamp': self.timing_instance.timestamp2})
                            break


                time.sleep(0.01)
        except KeyboardInterrupt:
            print("Exiting...")
        finally:
            self.bg.cleanup()


