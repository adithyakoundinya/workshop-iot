import RPi.GPIO as GPIO
import time 
GPIO.setmode(GPIO.BCM)

GPIO.setup(25,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(2,GPIO.OUT)

while True:
	GPIO.output(2,0)
	input_state = GPIO.input(25)
	if input_state == False:
		print "Button Pressed"
		#time.sleep(0.2)
		GPIO.output(2,1)
		time.sleep(1)
	else :
		GPIO.output(2,0)
		time.sleep(1)