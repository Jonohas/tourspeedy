import RPi.GPIO as GPIO
import time
from classes.Lights import Lights

lights = Lights()


    
try:
    lights.handle_lights([GPIO.HIGH, GPIO.LOW, GPIO.HIGH, GPIO.LOW])


finally:
    GPIO.cleanup()
