import threading
import time

from gpiozero import Button
import RPi.GPIO as GPIO

from classes.Singleton import Singleton


class SensorWatcher(threading.Thread, metaclass=Singleton):
    def __init__(self, timing_instance):
        super(SensorWatcher, self).__init__()

        self.timing_instance = timing_instance
        self.lock = threading.Lock()
        self.stop_event = threading.Event()  # Event to signal the thread to stop.
        self.button1 = Button(4)
        self.button2 = Button(5)

    def run(self):
        self.timing_instance.ready = True
        print("Starting SensorWatcher Thread...")
        while not self.stop_event.is_set():  # Check if the thread is signaled to stop.
            if self.button1.is_pressed:
                with self.lock:
                    if not self.timing_instance.timestamp1:
                        self.timing_instance.timestamp1 = time.time()
                        print("Start")
                        self.timing_instance.sio.emit('start', {'timestamp': self.timing_instance.timestamp1})

            if self.button2.is_pressed:
                with self.lock:
                    if not self.timing_instance.timestamp2 and self.timing_instance.timestamp1:
                        self.timing_instance.timestamp2 = time.time()
                        print("Stop:", (self.timing_instance.timestamp2 - self.timing_instance.timestamp1) * 1000, "milliseconds")
                        self.timing_instance.emit('stop', {'timestamp': self.timing_instance.timestamp2})


            time.sleep(0.01)
