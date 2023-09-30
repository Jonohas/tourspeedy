import threading
import time
import asyncio


from classes.Singleton import Singleton
from classes.ButtonGrid import ButtonGrid
from datetime import datetime, timezone
from classes.DB import add_event


class SensorWatcher(threading.Thread):
    def __init__(self, timing_instance):
        super(SensorWatcher, self).__init__()
        self.bg = ButtonGrid()


        self.timing_instance = timing_instance
        self.lock = threading.Lock()
        self.stop_event = threading.Event()  # Event to signal the thread to stop.


    def run(self):
        self.timing_instance.timestamp1 = None
        self.timing_instance.timestamp2 = None
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self.start_sensor_watch())
        
        self.timing_instance.ready = False

    async def start_sensor_watch(self):
        self.timing_instance.ready = True
        try:
            while not self.stop_event.is_set():  # Check if the thread is signaled to stop.
                response = self.bg.scan()
                if not response[0][0]:
                    with self.lock:
                        if not self.timing_instance.timestamp1:

                            dt1 = datetime.now()
                            self.timing_instance.timestamp1 = dt1
                            await self.timing_instance.sio.emit('start', {'start': self.timing_instance.timestamp1.timestamp()})

                if not response[0][1]:
                    with self.lock:
                        if not self.timing_instance.timestamp2 and self.timing_instance.timestamp1:
                            
                            dt2 = datetime.now()
                            self.timing_instance.timestamp2 = dt2
                            await self.timing_instance.sio.emit('stop', {'stop': self.timing_instance.timestamp2.timestamp()})
                            break

                await self.timing_instance.sio.emit("timestamp", {"timestamp": time.time()})


                time.sleep(0.01)
        except KeyboardInterrupt:
            print("Exiting...")
        finally:
            self.bg.cleanup()


