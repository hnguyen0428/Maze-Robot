import RPi.GPIO as GPIO, time

from motor import *

frs = 18
rs = 13
ms = 11
ls = 12
fls = 7
<<<<<<< HEAD
buttonpin = 22

def setup():
	print buttonpin
=======


def setup():
>>>>>>> 858e4576361617b31f39a7eab6ae2a267624c467
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(frs, GPIO.IN)
        GPIO.setup(rs, GPIO.IN)
        GPIO.setup(ms, GPIO.IN)
        GPIO.setup(ls, GPIO.IN)
        GPIO.setup(fls, GPIO.IN)
<<<<<<< HEAD
	GPIO.setup(buttonpin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
=======

>>>>>>> 858e4576361617b31f39a7eab6ae2a267624c467

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

<<<<<<< HEAD
=======

def moveFor(secs):
	forward(9)
	time.sleep(secs)
	stopall()

>>>>>>> 858e4576361617b31f39a7eab6ae2a267624c467
def shiftLeft():
	turn(10,0)
	time.sleep(0.2)
	stopall()

def shiftRight():
	turn(0,10)
	time.sleep(0.2)
	stopall()
<<<<<<< HEAD

speed = 13
=======
	
def moveInLine2():
	if GPIO.input(ms)==1 and GPIO.input(ls) == 0:
		forward(10)
		time.sleep(0.1)
	if GPIO.input(ls)==1:
		shiftRight()
	if GPIO.input(rs)==1:
		shiftLeft()

speed = 12
>>>>>>> 858e4576361617b31f39a7eab6ae2a267624c467
		
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

<<<<<<< HEAD
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

=======
orientation = ['north', 'east', 'south', 'west']
robotOrientation = orientation[1]
xcord = 0.0
ycord = 0.0
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
g=[]

def moveandTurn2():
	global xcord, ycord, robotOrientation, g
	state = 0
	nodeCounter = 0
	while True:
		if state == 0:
      goStraight()
			if GPIO.input(frs) == 1 and GPIO.input(ms) == 1 and GPIO.input(rs) == 1: #left and front are open
				state = 0
				g.append('S')
			if GPIO.input(frs) == 1 and GPIO.input(fls) == 1: #left and right are open
				state = 1
				g.append('R')
			if GPIO.input(fls) == 1 and GPIO.input(frs) == 0 and GPIO.input(ms) == 0: #right is open, left is closed
				state = 1
				g.append('R')
			if GPIO.input(fls) == 1 and GPIO.input(frs) == 1 and GPIO.input(ms) == 1: #4-way intersection
        state = 1
        g.append('R')                        
      if GPIO.input(fls) == 1 and GPIO.input(ms) == 1: #right and front are open
        state = 1
        g.append('R')                        
      if GPIO.input(fls) == 0 and GPIO.input(ms) == 0 and GPIO.input(frs) == 0 and GPIO.input(ls) == 0 and GPIO.input(rs) == 0: #deadend
        state = 3
        g.append('B')                        
      if GPIO.input(frs) == 1 and GPIO.input(fls) == 0 and GPIO.input(ms) == 0: #left is open, right is closed
				if GPIO.input(ms) != 1:
					shiftRight()
        if GPIO.input(ms) == 1:
					state = 0
					g.append('S')
				else:
					state = 2
					g.append('L')
			if GPIO.input(ms) == 0 and GPIO.input(fls) == 0 and GPIO.input(ls) == 1 and GPIO.input(rs) == 1 and GPIO.input(frs) == 0:
				state = 5
				stopall()
				return
		if state == 1: #turn right
			turnRight()
			if robotOrientation == 'west':
        robotOrientation = orientation[0]
      else:
        robotOrientation = orientation[orientation.index(robotOrientation) + 1]
			align()
			state = 0
			time.sleep(0.2)
			startTime = endTime
		if state == 2: #turn left
      turnLeft()
      if robotOrientation == 'north':
        robotOrientation = orientation[3]
      else:
        robotOrientation = orientation[orientation.index(robotOrientation) - 1]
			align()
      state = 0
			time.sleep(0.2)
			startTime=endTime
    if state == 3: #turn around
      turnTR()
      if robotOrientation == 'north' or robotOrientation == 'east':
        robotOrientation = orientation[orientation.index(robotOrientation) + 2]
      elif robotOrientation == 'south' or robotOrientation == 'west':
        robotOrientation = orientation[orientation.index(robotOrientation) - 2]
			align()
      state = 0
			time.sleep(0.2)
def shortenList(x):
  for letters in x[0:3]:
    if x[0:3]==['R', 'B', 'L']:
      x.remove('L')
      x.remove('B')
      x.remove('R')
      x.insert(0, 'B')
    if x[0:3]==['R', 'B', 'S']:
      x.remove('S')
      x.remove('B')
      x.remove('R')
      x.insert(0, 'L')
    if x[0:3]==['L', 'B', 'R']:
      x.remove('R')
      x.remove('B')
      x.remove('L')
      x.insert(0, 'B')
    if x[0:3]==['S', 'B', 'R']:
      x.remove('R')
      x.remove('B')
      x.remove('S')
      x.insert(0, 'L')
    if x[0:3]==['S', 'B', 'S']:
      x.remove('S')
      x.remove('B')
      x.remove('S')
      x.insert(0, 'B')
    if x[0:3]==['R', 'B', 'R']:
      x.remove('R')
      x.remove('B')
      x.remove('R')
      x.insert(0, 'S')
    shortenList(x[3:])
>>>>>>> 858e4576361617b31f39a7eab6ae2a267624c467
def destroy():
        GPIO.cleanup()

if __name__ == '__main__':
        setup()
        try:
<<<<<<< HEAD
                startMaze()
                
=======
                moveandTurn2()
                start=(0.0,0.0)
                end=(xcord,ycord)
		print g
		time.sleep(15)
                shortestPath(g,start,end)
                moveShortestPath(Path)
>>>>>>> 858e4576361617b31f39a7eab6ae2a267624c467
        except KeyboardInterrupt:
                destroy()


<<<<<<< HEAD
=======

>>>>>>> 858e4576361617b31f39a7eab6ae2a267624c467
