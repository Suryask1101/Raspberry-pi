import RPi.GPIO as GPIO
import time

# Set GPIO mode
GPIO.setmode(GPIO.BCM)

# Define GPIO pins
TRIG = 17
ECHO = 18

# Set up GPIO pins
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def get_distance():
    # Set TRIG to LOW for a short duration to ensure a clean pulse
    GPIO.output(TRIG, False)
    time.sleep(0.01)

    # Send a 10us pulse to trigger the sensor
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    # Measure the duration of the pulse from the ECHO pin
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    # Calculate pulse duration and convert to distance
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150  # Speed of sound is 343m/s, so 34300cm/s. Distance = time * speed / 2 (round trip)
    distance = round(distance, 2)  # Round to 2 decimal places

    return distance

try:
    while True:
        distance = get_distance()
        print("Distance:", distance, "cm")
        time.sleep(1)  # Wait for 1 second before next reading

except KeyboardInterrupt:
    GPIO.cleanup()  # Clean up GPIO on keyboard interrupt
