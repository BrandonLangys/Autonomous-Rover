#-------------------------------------#
#Brandon Langys                       #
#ROBOT_PROJECT                        #
#                                     #
#                                     #
#                                     #
#-------------------------------------#
from gpiozero import DistanceSensor #import for UltraSonic Sensor
from gpiozero import PWMOutputDevice #import for DC motors
from gpiozero import Servo
import pigpio # import for more accurate servo
from time import sleep
GPIO_TRIGGER = 23
GPIO_ECHO = 24
PWM_FORWARD_LEFT_PIN = 17	# IN1 - Forward Drive
PWM_REVERSE_LEFT_PIN = 22	# IN2 - Reverse Drive
PWM_FORWARD_RIGHT_PIN = 21	# IN1 - Forward Drive
PWM_REVERSE_RIGHT_PIN = 25	# IN2 - Reverse Drive

pi = pigpio.pi()





#-------------------------------------- Assign Speed for the PWM


forwardLeft = PWMOutputDevice(PWM_FORWARD_LEFT_PIN, True, 0, 1000)
reverseLeft = PWMOutputDevice(PWM_REVERSE_LEFT_PIN, True, 0, 1000)
forwardRight = PWMOutputDevice(PWM_FORWARD_RIGHT_PIN, True, 0, 1000)
reverseRight = PWMOutputDevice(PWM_REVERSE_RIGHT_PIN, True, 0, 1000)
sensor = DistanceSensor(echo=24, trigger=23)
pi.set_mode(12, pigpio.OUTPUT)



#--------------------------------------
def reverse():
    forwardLeft.value = 0
    reverseLeft.value = 1.0
    forwardRight.value = 0
    reverseRight.value = 1.0
    
				
#-------------------------------------
def forward():
    forwardLeft.value = 0.3
    reverseLeft.value = 0
    forwardRight.value = 0.55
    reverseRight.value = 0
   
#-------------------------------------				
def stop():
    forwardLeft.value = 0
    reverseLeft.value = 0
    forwardRight.value = 0
    reverseRight.value = 0
#-------------------------------------    	
def spinRight():
    forwardLeft.value = 0.8
    reverseLeft.value = 0
    forwardRight.value = 0
    reverseRight.value = 0.8
 #-------------------------------------   
    sleep(.5)
def spinLeft():
    forwardLeft.value = 0
    reverseLeft.value = 0.9
    forwardRight.value = 0.9
    reverseRight.value = 0
   
    sleep(1.2)
#-------------------------------------	
def distance():
    distance = sensor.distance *100
	
    return distance
#-------------------------------------
def servoRight():
    pi.set_servo_pulsewidth(12, 500)
    pi.get_servo_pulsewidth(12)
    print("servoRight")
#-------------------------------------	
def servoMid():
    pi.get_mode(12)
    pi.set_servo_pulsewidth(12, 1500)
    pi.get_servo_pulsewidth(12)
    
#-------------------------------------	
def servoLeft():
    pi.set_servo_pulsewidth(12, 2500)
    pi.get_servo_pulsewidth(12)
    print("servoLeft")
#-------------------------------------	
def checkDist():
	dist = sensor.distance*100
	print(dist)
	if(dist < 30):
		return False
	return True	
def main(): 
	try:
		while True:
		    servoMid()
		    rightCheck = False
		    leftCheck = False
		    forward()
		    dist = distance()
		    if(dist < 40):
			    stop()
			    servoRight()
			    sleep(3)
			    rightCheck = checkDist()
			    servoLeft()
			    sleep(3)
			    leftCheck = checkDist()
								
			    if(rightCheck): # check if there is an obstruction right side
				    print(rightCheck)
				    spinRight()
									
			    elif(leftCheck): # check if there is an obstruction left side
				    print(leftCheck)
				    spinLeft()
				    
		    print ("Measured Distance = %.1f cm" % dist)
		    sleep(.001)

        # Reset by pressing CTRL + C
	except KeyboardInterrupt:
		print("Measurement stopped by User")
		
#-------------------------------------
if __name__ == '__main__':
    main()
