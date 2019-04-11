#-------------------------------------#
#Created by:Brandon Langys            #
#ROBOT_PROJECT                        #
#Intro To RObotics                    #
#                                     #
#                                     #
#-------------------------------------#



from gpiozero import LightSensor
from time import sleep

ldr = LightSensor(26)
def returnLight():
    light = ldr.value

    if(light == 0.0):
        return ("Dark")
    return ("Light")
