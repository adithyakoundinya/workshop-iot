from RPi import GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(25,GPIO.OUT)
GPIO.setup(2,GPIO.OUT)
GPIO.setup(3,GPIO.OUT)
while True:
        GPIO.output(25,1)
        sleep(1)
        GPIO.output(25,0)
        sleep(1)
	GPIO.output(2,1)
	sleep(1)
	GPIO.output(2,0)
	sleep(1)
	GPIO.output(3,1)
	sleep(1)
	GPIO.output(3,0)
	sleep(1)
