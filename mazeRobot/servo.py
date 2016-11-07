import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD) # use physical numbering

def setupServo(servoPin):
   GPIO.setup(servoPin,GPIO.OUT)
   pwm=GPIO.PWM(servoPin, 50)
   return pwm
   
def setServoAngle(pwmSig, angle):
   if angle <0:
       print "Smallest possible angle is zero"
       angle = 0
   if angle > 180:
       print "Largest possible angle is 180 degrees"
       angle = 180
   # Full left (angle zero) requires a pulse width of 1 millisecond for PWM period of 20 millisec (or 50 Hz)
   # Full right (180 degrees) requires a pulse width of 2 millisecond for PWM period of 20 millisec (or 50 Hz)
   
   dutycycle = 5.0 + angle* 5.0/180.0
   pwmSig.ChangeDutyCycle(dutycyle)
