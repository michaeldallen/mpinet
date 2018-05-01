import RPi.GPIO as GPIO
import time
import readchar

from threading import Thread

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

def blink(pin, delay, cycles = 0):
    if cycles:
        for x in range(0,cycles):
            GPIO.output(pin, GPIO.HIGH)
            time.sleep(delay)
            GPIO.output(pin, GPIO.LOW)
            time.sleep(delay)
    else:
        while True:
            GPIO.output(pin, GPIO.HIGH)
            time.sleep(delay)
            GPIO.output(pin, GPIO.LOW)
            time.sleep(delay)
            

blueThread = Thread(target = blink, args=(7, 0.1))
blueThread.daemon=True
blueThread.start()

yellowThread = Thread(target = blink, args=(11, 2))
yellowThread.daemon = True
yellowThread.start()

redThread = Thread(target = blink, args=(13, 1))
redThread.daemon = True
redThread.start()

readchar.readkey()

GPIO.cleanup()


