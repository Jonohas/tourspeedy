from gpiozero import Button
import RPi.GPIO as GPIO
import time
import keyboard

# GPIO.setup(6, GPIO.IN, GPIO.PUD_DOWN)

button1 = Button(4) 
button2 = Button(5) 

count = 0

timestamp1 = None
timestamp2 = None


while True:
    if button1.is_pressed:
        if not timestamp1:
            timestamp1 = time.time()
            print("Start")

    if button2.is_pressed:
        if not timestamp2 and timestamp1: 
            timestamp2 = time.time()
            print("Stop:", (timestamp2 - timestamp1) * 1000, "milliseconds")

    if keyboard.is_pressed('r'):  # if key 'r' is pressed 
        print('Resetting')
        timestamp1 = None
        timestamp2 = None


