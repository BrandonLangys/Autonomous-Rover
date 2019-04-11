#-------------------------------------#
#Created by:Brandon Langys            #
#ROBOT_PROJECT                        #
#Intro To RObotics                    #
#                                     #
#                                     #
#-------------------------------------#




from gpiozero import PWMOutputDevice #import for DC motors
from time import sleep

PWM_FORWARD_LEFT_PIN = 17	# IN1 - Forward Drive
PWM_REVERSE_LEFT_PIN = 22	# IN2 - Reverse Drive
PWM_FORWARD_RIGHT_PIN = 21	# IN1 - Forward Drive
PWM_REVERSE_RIGHT_PIN = 25	# IN2 - Reverse Drive

forwardLeft = PWMOutputDevice(PWM_FORWARD_LEFT_PIN, True, 0, 1000)
reverseLeft = PWMOutputDevice(PWM_REVERSE_LEFT_PIN, True, 0, 1000)
forwardRight = PWMOutputDevice(PWM_FORWARD_RIGHT_PIN, True, 0, 1000)
reverseRight = PWMOutputDevice(PWM_REVERSE_RIGHT_PIN, True, 0, 1000)


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
    forwardLeft.value = 0.9
    reverseLeft.value = 0
    forwardRight.value = 0
    reverseRight.value = 0.9
    sleep(1)
 #-------------------------------------

def spinLeft():
    forwardLeft.value = 0
    reverseLeft.value = 0.9
    forwardRight.value = 0.9
    reverseRight.value = 0
    sleep(1)
