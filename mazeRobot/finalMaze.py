import RPi.GPIO as GPIO, time

from motor import *

frs = 18
rs = 13
ms = 11
ls = 12
fls = 7
buttonpin = 22

def setup():
	print buttonpin
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(frs, GPIO.IN)
        GPIO.setup(rs, GPIO.IN)
        GPIO.setup(ms, GPIO.IN)
        GPIO.setup(ls, GPIO.IN)
        GPIO.setup(fls, GPIO.IN)
	GPIO.setup(buttonpin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def turnLeft():
        turn(18,0)
	time.sleep(1)
	stopall()

def turnRight():
	turn(0,18)
	time.sleep(1)
	stopall()

def turnTR():
	while GPIO.input(ms) != 1:
		turnToRight(20, 20)
	stopall()

def shiftLeft():
	turn(10,0)
	time.sleep(0.2)
	stopall()

def shiftRight():
	turn(0,10)
	time.sleep(0.2)
	stopall()

speed = 13
		
def goStraight():
	if GPIO.input(ls) == 0 and GPIO.input(ms) == 1:
		forward(speed)
		
	
	if GPIO.input(ls) == 1 and GPIO.input(fls) == 0:
                shiftRight()
        if GPIO.input(rs) == 1 and GPIO.input(frs) == 0:
                shiftLeft()

def align():
	while GPIO.input(ls) == 1 and GPIO.input(ms) != 1:
		shiftRight()
	while GPIO.input(rs) == 1 and GPIO.input(ms) != 1:
		shiftLeft()
	while GPIO.input(fls) == 1:
		shiftRight()
	while GPIO.input(frs) == 1:
		shiftLeft()

def moveandTurn2():
	state = 0
	while True:
		if state == 0:
			goStraight()
			if GPIO.input(frs) == 1 and GPIO.input(ms) == 1 and GPIO.input(rs) == 1: #left and front are open
				state = 0
				
			if GPIO.input(frs) == 1 and GPIO.input(fls) == 1: #left and right are open
				state = 1
				
			if GPIO.input(fls) == 1 and GPIO.input(frs) == 0 and GPIO.input(ms) == 0: #right is open, left is closed
				state = 1
				     
			if GPIO.input(fls) == 1 and GPIO.input(frs) == 1 and GPIO.input(ms) == 1: #4-way intersection
                                state = 1
                                
                        if GPIO.input(fls) == 1 and GPIO.input(ms) == 1: #right and front are open
                                state = 1
                                
                        if GPIO.input(fls) == 0 and GPIO.input(ms) == 0 and GPIO.input(frs) == 0 and GPIO.input(ls) == 0 and GPIO.input(rs) == 0: #deadend
                                state = 3
                                
                        if GPIO.input(frs) == 1 and GPIO.input(fls) == 0 and GPIO.input(ms) == 0: #left is open, right is closed
				if GPIO.input(ms) != 1:
					shiftRight()
                                	if GPIO.input(ms) == 1:
						state = 0
					else:
						state = 2
						
			if GPIO.input(ms) == 0 and GPIO.input(fls) == 0 and GPIO.input(ls) == 1 and GPIO.input(rs) == 1 and GPIO.input(frs) == 0:
				state = 5
				stopall()
				break
		
		if state == 1: #turn right
			turnRight()
			align()
			state = 0
			time.sleep(0.1)
		if state == 2: #turn left
                        turnLeft()
			align()
                        state = 0
			time.sleep(0.1)
			
                if state == 3: #turn around
                        turnTR()
			align()
                        state = 0
			time.sleep(0.1)


def startMaze():
	state = 0
	while True:
		print GPIO.input(buttonpin)
		if state == 0 and GPIO.input(buttonpin) == False:
			moveandTurn2()
			state = 1		

def destroy():
        GPIO.cleanup()

if __name__ == '__main__':
        setup()
        try:
                startMaze()
                
        except KeyboardInterrupt:
                destroy()


