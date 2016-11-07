import RPi.GPIO as GPIO, time

from motor import *

farrightsensor = 18
rightsensor = 13
middlesensor = 11
leftsensor = 12
farleftsensor = 7
def setup():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(farrightsensor, GPIO.IN)
	GPIO.setup(rightsensor, GPIO.IN)
	GPIO.setup(middlesensor, GPIO.IN)
	GPIO.setup(leftsensor, GPIO.IN)
	GPIO.setup(farleftsensor, GPIO.IN)


def moveandTurn():
	while True:
		if GPIO.input(middlesensor) == 0:
			forward(20)
			print GPIO.input(middlesensor)
			time.sleep(0.1)
		stopall()
		if GPIO.input(middlesensor) == 1:
			print GPIO.input(middlesensor)
			turn(0,30)
			time.sleep(0.5)
			stopall()
			
def prt():
	while True:
		print GPIO.input(middlesensor)

def destroy():
	GPIO.cleanup()

if __name__ == '__main__':
	setup()
	try:
		moveandTurn()
	except KeyboardInterrupt:
		destroy()
