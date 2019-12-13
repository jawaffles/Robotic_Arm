#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Joy
import gantry
    
g = gantry.Gantry()




#Initial State of the the gantry robot
x = 50
y = 50

#Initial State of Dynamixel
Dyna1 = 1
Dyna2 = 2



#Proportional Value to control speed of position increment
p_increm = .5
arm_1_increm = 1
arm_2_increm = 1



def callback(joy):
##    rospy.loginfo("x:  %f", joy.axes[0])
##    rospy.loginfo("y:  %f", joy.axes[1])
    
    global x
    global y
    global p_increm

    x = x + (joy.axes[0] * -p_increm)
    
    if x > 100:
        x = 100
    if x < 0:
        x = 0
    if y > 100:
        y = 100
    if y < 0:
        y == 0
    rospy.loginfo("x:  %f", x)
    rospy.loginfo("y:  %f", y)    
    g.move(y,x)




def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("joy", Joy, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
