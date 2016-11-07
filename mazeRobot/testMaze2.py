import RPi.GPIO as GPIO, time

from motor import *

frs = 18
rs = 13
ms = 11
ls = 12
fls = 7


def setup():
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(frs, GPIO.IN)
        GPIO.setup(rs, GPIO.IN)
        GPIO.setup(ms, GPIO.IN)
        GPIO.setup(ls, GPIO.IN)
        GPIO.setup(fls, GPIO.IN)


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


def moveFor(secs):
	forward(9)
	time.sleep(secs)
	stopall()

def shiftLeft():
	turn(10,0)
	time.sleep(0.2)
	stopall()

def shiftRight():
	turn(0,10)
	time.sleep(0.2)
	stopall()
	
def moveInLine2():
	if GPIO.input(ms)==1 and GPIO.input(ls) == 0:
		forward(10)
		time.sleep(0.1)
	if GPIO.input(ls)==1:
		shiftRight()
	if GPIO.input(rs)==1:
		shiftLeft()

speed = 12
		
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
g={}
def GraphDict((oldx, oldy), (xcord, ycord), nodeLength):
	global g
	if (oldx, oldy) in g:
		g[(oldx, oldy)].update({(xcord, ycord):nodeLength})
	else:
		g[(oldx, oldy)]=({(xcord, ycord):nodeLength})
	if (xcord, ycord) in g:
		g[(xcord, ycord)].update({(oldx, oldy):nodeLength})
	else:
		g[(xcord, ycord)]=({(oldx, oldy):nodeLength})
	print g
startTime=time.time()
def moveandTurn2():
	global xcord, ycord, robotOrientation, startTime
	state = 0
	nodeCounter = 0
	while True:
		if state == 0:
                        startTime = time.time()
			goStraight()
			if GPIO.input(frs) == 1 and GPIO.input(ms) == 1 and GPIO.input(rs) == 1: #left and front are open
				state = 0
				endTime = time.time()
				nodeLength = (endTime - startTime)
				distance = (endTime - startTime)*speed
				oldx=xcord
				oldy=ycord
				updateCord(distance)
				GraphDict((oldx, oldy), (xcord, ycord), nodeLength)
			if GPIO.input(frs) == 1 and GPIO.input(fls) == 1: #left and right are open
				state = 1
				endTime = time.time()
				nodeLength = (endTime - startTime)
				distance = (endTime - startTime)*speed
				oldx=xcord
				oldy=ycord
				updateCord(distance)
				GraphDict((oldx, oldy), (xcord, ycord), nodeLength)
				
			if GPIO.input(fls) == 1 and GPIO.input(frs) == 0 and GPIO.input(ms) == 0: #right is open, left is closed
				state = 1
				endTime = time.time()
				nodeLength = (endTime - startTime)
				distance = (endTime - startTime)*speed
				oldx=xcord
				oldy=ycord
				updateCord(distance)
				GraphDict((oldx, oldy), (xcord, ycord), nodeLength)
				
			if GPIO.input(fls) == 1 and GPIO.input(frs) == 1 and GPIO.input(ms) == 1: #4-way intersection
                                state = 1
                                endTime = time.time()
				nodeLength = (endTime - startTime)
				distance = (endTime - startTime)*speed
				oldx=xcord
				oldy=ycord
				updateCord(distance)
				GraphDict((oldx, oldy), (xcord, ycord), nodeLength)
                                
                        if GPIO.input(fls) == 1 and GPIO.input(ms) == 1: #right and front are open
                                state = 1
                                endTime = time.time()
				nodeLength = (endTime - startTime)
				distance = (endTime - startTime)*speed
				oldx=xcord
				oldy=ycord
				updateCord(distance)
				GraphDict((oldx, oldy), (xcord, ycord), nodeLength)
                                
                        if GPIO.input(fls) == 0 and GPIO.input(ms) == 0 and GPIO.input(frs) == 0 and GPIO.input(ls) == 0 and GPIO.input(rs) == 0: #deadend
                                state = 3
                                endTime = time.time()
				nodeLength = (endTime - startTime)
				distance = (endTime - startTime)*speed
				oldx=xcord
				oldy=ycord
				updateCord(distance)
				GraphDict((oldx, oldy), (xcord, ycord), nodeLength)
                                
                        if GPIO.input(frs) == 1 and GPIO.input(fls) == 0 and GPIO.input(ms) == 0: #left is open, right is closed
				if GPIO.input(ms) != 1:
					shiftRight()
                                	if GPIO.input(ms) == 1:
						state = 0
					else:
						state = 2
						endTime = time.time()
                                                nodeLength = (endTime - startTime)
						distance = (endTime - startTime)*speed
						oldx=xcord
						oldy=ycord
						updateCord(distance)
						GraphDict((oldx, oldy), (xcord, ycord), nodeLength)
						
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
			startTime = endTime
from priodict import priorityDictionary
def Dijkstra(G,start,end=None):
	D = {}	# dictionary of final distances
	P = {}	# dictionary of predecessors
	Q = priorityDictionary()   # est.dist. of non-final vert.
	Q[start] = 0
	for v in Q:
		D[v] = Q[v]
		if v == end: break
		
		for w in G[v]:
			vwLength = D[v] + G[v][w]
			if w in D:
				if vwLength < D[w]:
					raise ValueError, \
  "Dijkstra: found better path to already-final vertex"
			elif w not in Q or vwLength < Q[w]:
				Q[w] = vwLength
				P[w] = v
	
	return (D,P)
Path = []
def shortestPath(G,start,end):
	D,P = Dijkstra(G,start,end)
	global Path 
	while 1:
		Path.append(end)
		if end == start: break
		end = P[end]
	Path.reverse()
	
	

def moveShortestPath(pathList):
	#fix orienation problem!!!!
	robotOrientation=orientation[1]
	for cord in pathList:
		for i in range(len(pathList)-1):
			if pathList[i+1][1]==pathList[i][1]:
				if pathList[i+1][0]>pathList[i][0]:
					if robotOrientation==orientation[1]:
						forward(pathList[i+1][0]/speed)
					if robotOrientation==orientation[0]:
						turnRight()
						if robotOrientation == 'west':
                					robotOrientation = orientation[0]
                				else:
                					robotOrientation = orientation[orientation.index(robotOrientation) + 1]
						align()
						state = 0
						time.sleep(0.2)
						forward(pathList[i+1][0]/speed)
					if robotOrientation==orientation[2]:
						turnLeft()
						if robotOrientation == 'north':
                        				robotOrientation = orientation[3]
                				else:
                        				robotOrientation = orientation[orientation.index(robotOrientation) - 1]
						align()
                				state = 0
						time.sleep(0.2)
						forward(pathList[i+1][0]/speed)
				if pathList[i+1][0]<pathList[i][0]:
					if robotOrientation==orientation[3]:
						forward(pathList[i+1][0]/speed)
					if robotOrientation==orientation[0]:
						turnLeft()
						forward(pathList[i+1][0]/speed)
					if robotOrientation==orientation[2]:
						turnRight()
						forward(pathList[i+1][0]/speed)
			else:
				if pathList[i+1][1]>pathList[i][1]:
					if robotOrientation==orientation[0]:
						forward(pathList[i+1][0]/speed)
					if robotOrientation==orientation[1]:
						turnLeft()
						forward(pathList[i+1][0]/speed)
					if robotOrientation==orientation[3]:
						turnRight()
						forward(pathList[i+1][0]/speed)
				if pathList[i+1][1]<pathList[i][1]:
					if robotOrientation==orientation[2]:
						forward(pathList[i+1][0]/speed)
					if robotOrientation==orientation[3]:
						turnLeft()
						forward(pathList[i+1][0]/speed)
					if robotOrientation==orientation[1]:
						turnRight()
						forward(pathList[i+1][0]/speed)

	
def destroy():
        GPIO.cleanup()

if __name__ == '__main__':
        setup()
        try:
                moveandTurn2()
                start=(0.0,0.0)
                end=(xcord,ycord)
		print g
		time.sleep(15)
                shortestPath(g,start,end)
                moveShortestPath(Path)
        except KeyboardInterrupt:
                destroy()


