

import RPi.GPIO as GPIO
import time
from classes.Singleton import Singleton

class Lights(metaclass=Singleton):
    
    def __init__(self):
        if not hasattr(self, 'light_pins'):
            self.light_pins = [14, 15, 18, 23]
            GPIO.setmode(GPIO.BCM)
            self.setup()



    def setup(self):
        # Setting up row pins as output and initializing them to HIGH
        for pin in self.light_pins:
            GPIO.setup(pin, GPIO.OUT)
        self.handle_lights([ GPIO.LOW, GPIO.LOW ,GPIO.LOW, GPIO.LOW ])
        

    def handle_lights(self, values = [GPIO.LOW, GPIO.LOW, GPIO.LOW, GPIO.LOW]):
        for i, light_pin in enumerate(self.light_pins):
            GPIO.output(light_pin, not values[i])

    
    def cleanup(self):
        self.handle_lights([ GPIO.LOW, GPIO.LOW ,GPIO.LOW, GPIO.LOW ])
        GPIO.cleanup()
