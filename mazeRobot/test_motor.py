# Pizazz Motor Test
# Moves: Forward, Reverse, turn Right, turn Left, Stop - then repeat
# Press Ctrl-C to stop
#
# To check wiring is correct ensure the order of movement as above is correct
# Run using: sudo python motorTest.py


import RPi.GPIO as GPIO, time

from motor import *
#use physical pin numbering
GPIO.setmode(GPIO.BOARD)

# main loop
try:
  while True:
    forward(50)
    time.sleep(2)
    reverse(50)
    time.sleep(2)
    turn(rspeed= 20, lspeed =50)
    time.sleep(2)
    turn(rspeed = 50, lspeed = 20)
    time.sleep(2)
    stopall()
    time.sleep(10)

except KeyboardInterrupt:
    GPIO.cleanup()
