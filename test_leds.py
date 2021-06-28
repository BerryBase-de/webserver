import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library

from time import sleep     # Import the sleep function from the time module

GPIO.setwarnings(False)    # Ignore warning for now

GPIO.setmode(GPIO.BCM)     #BCM Mode

GPIO.setup(20, GPIO.OUT)   #GPIO 20 as output
GPIO.setup(21, GPIO.OUT)   #GPIO 21 as output

for x in range(2):             # Blink 2 times 
    GPIO.output(20, GPIO.HIGH) # Turn on
    GPIO.output(21, GPIO.HIGH)
    sleep(1)                   # Sleep for 1 second
    GPIO.output(20, GPIO.LOW)  # Turn off
    GPIO.output(21, GPIO.LOW)
    sleep(1)
