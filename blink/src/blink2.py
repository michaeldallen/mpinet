import RPi.GPIO as GPIO
import time

# Configure the PIN # 8
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT)
GPIO.setwarnings(False)

# Blink Interval 
blink_interval = .1 #Time interval in Seconds

# Blinker Loop
scale=10.0
while True:
  for bi in range(-5, 5):
    GPIO.output(8, True)
    time.sleep(abs(bi/scale))
    GPIO.output(8, False)
    time.sleep(abs(bi/scale))

# Release Resources
GPIO.cleanup()
