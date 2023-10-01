import RPi.GPIO as GPIO
import time

class SensorGrid:
    
    def __init__(self):

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        self.setup()

    def setup(self):

        pass

    def scan(self):
        return [GPIO.input(5) == GPIO.HIGH, GPIO.input(6) == GPIO.HIGH]
    
    def cleanup(self):
        pass

# if __name__ == '__main__':
#     bg = ButtonGrid()
#     try:
#         while True:
#             bg.scan()
#             time.sleep(0.01)  # Sleep for a while to debounce and reduce CPU usage
#     except KeyboardInterrupt:
#         print("Exiting...")
#     finally:
#         bg.cleanup()
