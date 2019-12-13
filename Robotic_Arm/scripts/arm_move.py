#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from std_msgs.msg import Float64
import time 

def arm_reset():
    pub1.publish(0.0)
    time.sleep(1)
    pub2.publish(0.0)
    time.sleep(1)
    pub3.publish(0.0)
    time.sleep(1)
    pub4.publish(0.0)
    time.sleep(1)
    pubend.publish(0.0)





def arm_move():
    pub1 = rospy.Publisher('/Robotic_Arm/arm_joint_1_position_controller/command', Float64, queue_size=10)
    pub2 = rospy.Publisher('/Robotic_Arm/arm_joint_2_position_controller/command', Float64, queue_size=10)
    pub3 = rospy.Publisher('/Robotic_Arm/arm_joint_3_position_controller/command', Float64, queue_size=10)
    pub4 = rospy.Publisher('/Robotic_Arm/arm_joint_4_position_controller/command', Float64, queue_size=10)
    pubend = rospy.Publisher('/Robotic_Arm/arm_joint_end_position_controller/command', Float64, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
            pub1.publish(2.0)
            time.sleep(1)
            pub2.publish(-1.0)
            time.sleep(1)
            pub3.publish(-1.0)
            time.sleep(1)
            pub4.publish(-1.0)
            time.sleep(1)
            pubend.publish(-1.0)
            
            pub1.publish(0.0)
            time.sleep(1)
            pub2.publish(0.0)
            time.sleep(1)
            pub3.publish(0.0)
            time.sleep(1)
            pub4.publish(0.0)
            time.sleep(1)
            pubend.publish(0.0)

    



if __name__=='__main__':
    try:
        arm_move()
    except rospy.ROSInterruptException:
        pass