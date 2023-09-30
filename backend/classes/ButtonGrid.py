import RPi.GPIO as GPIO
import time

class ButtonGrid:
    
    def __init__(self):
        self.row_pins = [4]
        self.col_pins = [22, 6, 5, 13]
        GPIO.setmode(GPIO.BCM)
        self.setup()

        self.pressed = []

    def setup(self):
        # Setting up row pins as output and initializing them to HIGH
        for pin in self.row_pins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.HIGH)
        
        # Setting up column pins as input and enabling the internal pull-up resistor
        for pin in self.col_pins:
            GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def scan(self):
        rows_output = []
        for i, row_pin in enumerate(self.row_pins):
            GPIO.output(row_pin, GPIO.LOW)  # Activate one row at a time by setting it to LOW
            output = []
            for j, col_pin in enumerate(self.col_pins):
                output.append(GPIO.input(col_pin))
                
            GPIO.output(row_pin, GPIO.HIGH)  # Deactivate the row before moving to the next one
            rows_output.append(output)
        return rows_output
    
    def cleanup(self):
        GPIO.cleanup()

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
