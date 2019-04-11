#-------------------------------------#
#Created by:Brandon Langys            #
#ROBOT_PROJECT                        #
#Intro To RObotics                    #
#                                     #
#                                     #
#-------------------------------------#



from gpiozero import Servo
import pigpio # import for more accurate servo
pi = pigpio.pi()
pi.set_mode(12, pigpio.OUTPUT)




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
