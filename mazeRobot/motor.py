# Pizazz Motor functions 
# Moves: Forward, Reverse, turn Right, turn Left, Stop 

import RPi.GPIO as GPIO, time

#use physical pin numbering
GPIO.setmode(GPIO.BOARD)

slowspeed =20
fastspeed = 100
avgspeed = 50
rightTop = 19
rightBottom = 21
leftTop = 24
leftBottom = 26
#use pwm on inputs so motors don't go too fast
# Pins 19, 21 Right Motor
# Pins 24, 26 Left Motor
GPIO.setup(rightTop, GPIO.OUT)
GPIO.setup(rightBottom, GPIO.OUT)
GPIO.setup(leftTop, GPIO.OUT)
GPIO.setup(leftBottom, GPIO.OUT)

rightTopPWM=GPIO.PWM(rightTop, 20)
rightTopPWM.start(0)

rightBottomPWM=GPIO.PWM(rightBottom, 20)
rightBottomPWM.start(0)

leftTopPWM = GPIO.PWM(leftTop,20)
leftTopPWM.start(0)

leftBottomPWM=GPIO.PWM(leftBottom,20)
leftBottomPWM.start(0)

def forward(speed=avgspeed):
   rightTopPWM.ChangeDutyCycle(speed)
   rightBottomPWM.ChangeDutyCycle(0)
   leftTopPWM.ChangeDutyCycle(speed)
   leftBottomPWM.ChangeDutyCycle(0)
 
def reverse(speed=avgspeed):
   rightTopPWM.ChangeDutyCycle(0)
   rightBottomPWM.ChangeDutyCycle(speed)
   leftTopPWM.ChangeDutyCycle(0)
   leftBottomPWM.ChangeDutyCycle(speed)
 

def turn(rspeed=fastspeed,lspeed=slowspeed ):
   rightTopPWM.ChangeDutyCycle(rspeed)
   rightBottomPWM.ChangeDutyCycle(0)
   leftTopPWM.ChangeDutyCycle(lspeed)
   leftBottomPWM.ChangeDutyCycle(0)
  
def turnToRight(rspeed=fastspeed, lspeed=slowspeed):
   rightTopPWM.ChangeDutyCycle(rspeed)
   rightBottomPWM.ChangeDutyCycle(0)
   leftTopPWM.ChangeDutyCycle(0)
   leftBottomPWM.ChangeDutyCycle(lspeed)

def turnToLeft(rspeed=fastspeed,lspeed=slowspeed ):
   rightTopPWM.ChangeDutyCycle(0)
   rightBottomPWM.ChangeDutyCycle(rspeed)
   leftTopPWM.ChangeDutyCycle(lspeed)
   leftBottomPWM.ChangeDutyCycle(0)

def stopall():
   rightTopPWM.ChangeDutyCycle(0)
   rightBottomPWM.ChangeDutyCycle(0)
   leftTopPWM.ChangeDutyCycle(0)
   leftBottomPWM.ChangeDutyCycle(0)
  
