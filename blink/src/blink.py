import RPi.GPIO as GPIO
import time
import readchar
from threading import Thread

def flicker(ledPin, finalState = GPIO.LOW):
    for x in range(0,5):
        if (GPIO.input(ledPin)): 
            GPIO.output(ledPin, GPIO.LOW)
        else:
            GPIO.output(ledPin, GPIO.HIGH)
        time.sleep(0.02)


    

def button_press(channel):
    if(GPIO.input(buttonPin) == GPIO.input(ledPin)):
        flicker(ledPin)
    GPIO.output(ledPin, GPIO.input(buttonPin))



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
            

    

buttonPin = 37
ledPin = 36


GPIO.setmode(GPIO.BOARD)

GPIO.setup(        7, GPIO.OUT                            )
GPIO.setup(       11, GPIO.OUT                            )
GPIO.setup(       13, GPIO.OUT                            )
GPIO.setup(   ledPin, GPIO.OUT, initial=GPIO.HIGH         )

GPIO.setup(buttonPin,  GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


#GPIO.add_event_detect(buttonPin, GPIO.BOTH, bouncetime=20)
GPIO.add_event_detect(buttonPin, GPIO.BOTH)
GPIO.add_event_callback(buttonPin, button_press)




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


