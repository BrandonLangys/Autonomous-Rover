#-------------------------------------#
#Created by:Brandon Langys            #
#ROBOT_PROJECT                        #
#Intro To RObotics                    #
#                                     #
#                                     #
#-------------------------------------#
import moveFunction as move
import servoMove as servo
import distance as dist
from time import sleep

def checkLoc():
    servo.servoRight()
    var1 = dist.distance()
    sleep(1)
    servo.servoLeft()
    var2 = dist.distance()
    sleep(1)
    
