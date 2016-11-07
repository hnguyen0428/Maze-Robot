import RPi.GPIO as GPIO, time

# By default uses pin 8
SONAR = 8
def setupSonar(sonarPin=SONAR):
   #use physical pin numbering
   GPIO.setmode(GPIO.BOARD)
   # Define Sonar Pin for Trigger and Echo to be the same
   SONAR = sonarPin


def getDistance():

   GPIO.setup(SONAR, GPIO.OUT)
   GPIO.output(SONAR, True)
   time.sleep(0.00001)
   GPIO.output(SONAR, False)
   start = time.time()
   count = time.time()
   GPIO.setup(SONAR, GPIO.IN)
   while GPIO.input(SONAR)==0 and time.time()-count<0.1:
         start = time.time()
   stop=time.time()
   while GPIO.input(SONAR)==1:
         stop = time.time()
   # Calculate pulse length
   elapsed = stop-start
   # Distance pulse travelled in that time is time
   # multiplied by the speed of sound (cm/s)
   distance = elapsed * 34000
   # That was the distance there and back so halve the value
   distance = distance / 2
   return distance

