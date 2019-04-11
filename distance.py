#-------------------------------------#
#Created by:Brandon Langys            #
#ROBOT_PROJECT                        #
#Intro To RObotics                    #
#                                     #
#                                     #
#-------------------------------------#



from gpiozero import DistanceSensor #import for UltraSonic Sensor
GPIO_TRIGGER = 23
GPIO_ECHO = 24
sensor = DistanceSensor(echo=24, trigger=23)

#-------------------------------------
def distance():
    distance = sensor.distance *100

    return distance
#-------------------------------------
def checkDist():
	dist = sensor.distance*100
	print(dist)
	if(dist < 30):
		return False
	return True
