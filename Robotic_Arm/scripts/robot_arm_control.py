#!/usr/bin/env python
import ikpy 
import numpy as np
from ikpy import plot_utils
import matplotlib.pyplot as plt
import matplotlib
import rospy
from std_msgs.msg import Float64

from mpl_toolkits.mplot3d import Axes3D
ax = matplotlib.pyplot.figure().add_subplot(111, projection='3d')

my_chain = ikpy.chain.Chain.from_urdf_file("/home/biosensing/catkin_ws/src/Robotic_Arm/urdf/Robotic_Arm.urdf")

my_chain.active_links_mask[True,True,True,True,True,True]




def getJoints(x,y,z):
    # x = 0
    # y = 0
    # z = 1.5
    end_effector = [
        [1, 0, 0, x],
        [0, 1, 0, y],
        [0, 0, 1, z],
        [0, 0, 0, 1]
        ]
    test = my_chain.inverse_kinematics(end_effector)

    my_chain.plot(test, ax)
    matplotlib.pyplot.show()

    return test

# print(test)

# my_chain.plot(test, ax)
# matplotlib.pyplot.show()


def talker():
    arm1 = rospy.Publisher('/Robotic_Arm/arm_joint_1_position_controller/command', Float64, queue_size=10)
    arm2 = rospy.Publisher('/Robotic_Arm/arm_joint_2_position_controller/command', Float64, queue_size=10)
    arm3 = rospy.Publisher('/Robotic_Arm/arm_joint_3_position_controller/command', Float64, queue_size=10)
    arm4 = rospy.Publisher('/Robotic_Arm/arm_joint_4_position_controller/command', Float64, queue_size=10)
   

    joint = getJoints(0.5,.25,.5)
    
    
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        # hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo("arm_joint1: %f , arm_joint2: %f , arm_joint3: %f , arm_joint4: %f", joint[1], joint[2],joint[3],joint[4])
        arm1.publish(joint[1])
        arm2.publish(joint[2])
        arm3.publish(joint[3])
        arm4.publish(joint[4])

        rate.sleep()


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass



