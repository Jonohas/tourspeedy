from gpiozero import Button
import RPi.GPIO as GPIO
import time
import keyboard

# GPIO.setup(6, GPIO.IN, GPIO.PUD_DOWN)
# button1 = Button(4) 
# button2 = Button(5) 

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

count = 0

timestamp1 = None
timestamp2 = None



try:
    while True:
        if GPIO.input(23) == GPIO.HIGH:
            print("Sensor1")
            if not timestamp1:
                timestamp1 = time.time()
                print("Start")

        if GPIO.input(24) == GPIO.HIGH:
            print("Sensor2")
            if not timestamp2 and timestamp1: 
                timestamp2 = time.time()
                print("Stop:", (timestamp2 - timestamp1) * 1000, "milliseconds")

        if keyboard.is_pressed('r'):  # if key 'r' is pressed 
            print('Resetting')
            timestamp1 = None
            timestamp2 = None
        
except KeyboardInterrupt:
    print("Interrupted by user. Cleaning up...")
finally:
    GPIO.cleanup()





