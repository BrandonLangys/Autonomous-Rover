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
import light_sensor as light
from time import sleep

#counter = 0
def main():
	try:
		counter = 0
		while True:
		    servo.servoMid()
			lightReal = light.returnLight()
			if(lightReal == "Dark"):
				move.stop()
		    rightCheck = False
		    leftCheck = False
		    move.forward()
		    diss = dist.distance()
		    if(diss < 40):
			    move.stop()
			    servo.servoRight()
			    sleep(3)
			    rightCheck = dist.checkDist()
			    servo.servoLeft()
			    sleep(3)
			    leftCheck = dist.checkDist()

			    if(rightCheck): # check if there is an obstruction right side
				    print(rightCheck)
				    move.spinRight()

			    elif(leftCheck): # check if there is an obstruction left side
				    print(leftCheck)
				    move.spinLeft()
                    counter = counter + 1
		    if(counter == 15):
			    #counter = 1
			    var = light.returnLight()
			    print("Hey, it is " + var + " in here")
			    sleep(1)
		            counter = 0

		    print ("Measured Distance = %.1f cm" % diss)
		    #counter = counter + 1
		    sleep(.001)

        # Reset by pressing CTRL + C
	except KeyboardInterrupt:
		print("Measurement stopped by User")
