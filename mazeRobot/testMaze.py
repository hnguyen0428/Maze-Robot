import RPi.GPIO as GPIO, time

from motor import *

frs = 18
rs = 13
ms = 11
ls = 12
fls = 7
buttonpin = 8

def setup():
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

nodeLength = []
orientation = ['north', 'east', 'south', 'west']
robotOrientation = orientation[1]
xcord = 0.0
ycord = 0.0
nodeCord = []
nodeDict = {}
def updateCord(distance):
        global xcord, ycord, robotOrientation
        if robotOrientation == 'north':
                ycord = ycord + distance
        if robotOrientation == 'east':
                xcord = xcord + distance
        if robotOrientation == 'south':
                ycord = ycord - distance
        if robotOrientation == 'west':
                xcord = xcord - distance

nodeCounter = 0

def updateDict():
        global xcord, ycord, nodeCounter, nodeCord, nodeDict
        for i in nodeCord:
                if (xcord < i[0] + 5.0 and xcord > i[0] - 5.0) and (ycord < i[1] + 5.0 and ycord > i[0] - 5.0):
                        return
	nodeDict[nodeCounter] = nodeCord[len(nodeCord)-1]
        nodeCounter += 1
        print nodeDict
                       
                
startTime = time.time()

def moveandTurn2():
	global xcord, ycord, robotOrientation, nodeCord, nodeDict, nodeCounter, startTime
	state = 0
	while True:
		if state == 0:
			goStraight()
			if GPIO.input(frs) == 1 and GPIO.input(ms) == 1 and GPIO.input(rs) == 1: #left and front are open
				state = 4
				
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
			endTime = time.time()
                        nodeLength.append(endTime - startTime)
                        distance = (endTime - startTime)*speed
                        updateCord(distance)
                        nodeCord.append((xcord, ycord))
                        updateDict()
			if robotOrientation == 'west':
                                robotOrientation = orientation[0]
                        else:
                                robotOrientation = orientation[orientation.index(robotOrientation) + 1]
			align()
			state = 0
			time.sleep(0.1)
			startTime = endTime
		if state == 2: #turn left
                        turnLeft()
                        endTime = time.time()
                        nodeLength.append(endTime - startTime)
                        distance = (endTime - startTime)*speed
                        updateCord(distance)
                        nodeCord.append((xcord, ycord))
                        updateDict()
                        if robotOrientation == 'north':
                                robotOrientation = orientation[3]
                        else:
                                robotOrientation = orientation[orientation.index(robotOrientation) - 1]
			align()
                        state = 0
			time.sleep(0.1)
			startTime = endTime
                if state == 3: #turn around
                        turnTR()
                        endTime = time.time()
                        nodeLength.append(endTime - startTime)
                        distance = (endTime - startTime)*speed
                        updateCord(distance)
                        nodeCord.append((xcord, ycord))
                        updateDict()
                        if robotOrientation == 'north' or robotOrientation == 'east':
                                robotOrientation = orientation[orientation.index(robotOrientation) + 2]
                        elif robotOrientation == 'south' or robotOrientation == 'west':
                                robotOrientation = orientation[orientation.index(robotOrientation) - 2]
			align()
                        state = 0
			time.sleep(0.1)
			startTime = endTime
		if state == 4:
			forward(13)
			time.sleep(0.4)
			stopall()
			endTime = time.time()
			nodeLength.append(endTime - startTime)
			distance = (endTime - startTime)*speed
			updateCord(distance)
			nodeCord.append((xcord, ycord))
			updateDict()
			state = 0
			startTime = endTime

def destroy():
        GPIO.cleanup()

if __name__ == '__main__':
        setup()
        try:
                moveandTurn2()
                
        except KeyboardInterrupt:
                destroy()


