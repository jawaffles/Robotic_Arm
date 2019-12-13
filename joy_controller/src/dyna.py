#!/usr/bin/env python

import rospy
from joy_controller.srv import *
from dynamixel_workbench_msgs.msg import *
from sensor_msgs.msg import Joy
import os


#Controls Base
global joy3
#Controls Joint 1
global joy4
#Controls Joint 2
global joy5
#Controls Joint 3
global joy6
#Gripper Open
global joy9
#Gripper Close
global joy10

global state

joy3 = 0
joy4 = 0
joy5 = 0
joy6 = 0

joy9 = 0
joy10 = 0
state = 1 

def moveDyna(DynaID,position):
	#Move Dynamixel to the position inputted.
	rospy.wait_for_service('/dynamixel_workbench/dynamixel_command',10)
	command = ''
	addr_name = 'Goal_Position'

	try:
		dyna_call = rospy.ServiceProxy('/dynamixel_workbench/dynamixel_command', Command)
		print("Requesting position %d at id: %d")%(position, DynaID)
		resp1 = dyna_call(command,DynaID,addr_name,position)
		# rospy.sleep(2)
	
	except rospy.ServiceException, e:
		print("Service Call Failed: %s")%e


def changeState(input_state):
	global state
	if input_state == 1 and state != 1:
		os.system("rosnode kill dynamixel_workbench")
		os.system("roslaunch dynamixel_workbench_controllers dynamixel_controllers.launch")
		state = 1
		
	if input_state == 2 and state != 2:
		os.system("rosnode kill dynamixel_workbench")
		os.system("roslaunch dynamixel_workbench_controllers dynamixel_controllers2.launch")
		state = 2

	if input_state == 3 and state != 3:
		os.system("rosnode kill dynamixel_workbench")
		os.system("roslaunch dynamixel_workbench_controllers dynamixel_controllers3.launch")
		state = 3
	else:
		pass
	



def dynaCallback(data):
	#Controls Base
	global joy3
	#Controls Joint 1
	global joy4
	#Controls Joint 2
	global joy5
	#Controls Joint 3
	global joy6
	#Gripper Open
	global joy9
	#Gripper Close
	global joy10

	global state
	joy3_increm = 8000
	joy4_increm = 100

	# print("DynaID: %d is at position: %d")%(data.dynamixel_state[0].id,data.dynamixel_state[0].present_position)
	# print("DynaID: %d is at position: %d")%(data.dynamixel_state[1].id,data.dynamixel_state[1].present_position)
	

	#Controls base and joint 1 dynamixel
	if abs(joy3) > 0:
		if state != 1:
			changeState(1)
		print(int((data.dynamixel_state[0].present_position+ (joy3 * joy3_increm))))
		moveDyna(1,int((data.dynamixel_state[0].present_position+ (joy3 * joy3_increm))))
	if abs(joy4) > 0:
		if state != 1:
			changeState(1)
		print(int((data.dynamixel_state[1].present_position+ (joy4 * joy3_increm))))
		moveDyna(2,int((data.dynamixel_state[1].present_position+ (joy4 * joy3_increm))))
	
	#Controls joint 2 dynamixel
	if abs(joy5) > 0:
		if state != 2:
			changeState(2)
		print(int((data.dynamixel_state[0].present_position+ (joy5 * joy4_increm))))
		moveDyna(3,int((data.dynamixel_state[0].present_position+ (joy5 * joy4_increm))))

	#Controls joint 3 dynamixel
	if abs(joy6) > 0:
		if state != 2:
			changeState(2)
		print(int((data.dynamixel_state[1].present_position+ (joy6 * joy4_increm))))
		moveDyna(4,int((data.dynamixel_state[1].present_position+ (joy6 * joy4_increm))))



	#Controls gripper dynamixel
	if abs(joy9 + joy10) > 0:
		if state != 3:
			changeState(3)
		print(int((data.dynamixel_state[0].present_position+ ((joy9 + joy10) * joy4_increm))))
		moveDyna(5,int((data.dynamixel_state[0].present_position+ ((joy9 + joy10) * joy4_increm))))

	



	# dyna0 = data.dynamixel_state[0].present_position
	# dyna1 = data.dynamixel_state[1].present_position
	


def joyCallback(joy):
	#Controls Base
	global joy3
	#Controls Joint 1
	global joy4
	#Controls Joint 2
	global joy5
	#Controls Joint 3
	global joy6
	#Gripper Open
	global joy9
	#Gripper Close
	global joy10

	#Controls Base
	joy3 = joy.axes[2]
	
	#Controls Joint 1
	joy4 = joy.axes[3]

	#Controls Joint 2
	joy5 = joy.axes[4]
	
	#Controls Joint 3
	joy6 = joy.axes[5]

	#Gripper Open
	joy9 = joy.buttons[1]
	#Gripper Close
	joy10 = -1* joy.buttons[2]



	# print(joy3)
	# print(joy4)

	# base_increm = 1
	# # rospy.loginfo("moveDyna1:  %f", joy.axes[3])
	# # rospy.loginfo("moveDyna2:  %f", joy.axes[4])
	# dynaState1 = dyna0 + (joy.axes[3]  * base_increm)
	# dynaState2 = dyna1 + (joy.axes[4]  * base_increm)

	# moveDyna(1, round(dynaState1))
	# moveDyna(2, round(dynaState2))

	# print(dynaState1)
	# print(dynaState2)


def listener():
	rospy.init_node('Dynamixel_Control', anonymous=True)
	rospy.Subscriber("/dynamixel_workbench/dynamixel_state",DynamixelStateList, dynaCallback)		
	rospy.Subscriber("/joy", Joy, joyCallback)
	rospy.spin()


if __name__== '__main__':
	listener()
	

	
# 	d = Dyna()
# #	d.moveDyna(1, 60000)
# #	d.moveDyna(2, 50454)

# 	d.change34()
# 	d = Dyna()
# #	d.moveDyna(3, 2582)
# #	d.moveDyna(4, 3662)
	







	
# class Dyna:
	# 	def __init__(self):
	# 		#Read Current Positions of all Dynamixels
	# 		self.dyna0 = 0		
	# 		self.dyna1 = 0
	# 		dyna0 = 0
	# 		dyna1 = 0 		
	# 		self.readDyna()




	# 	def moveDyna(self,DynaID,position):
	# 		#Move Dynamixel to the position inputted.
	# 		rospy.wait_for_service('/dynamixel_workbench/dynamixel_command',5)
	# 		command = ''
	# 		addr_name = 'Goal_Position'

	# 		try:
	#  			dyna_call = rospy.ServiceProxy('/dynamixel_workbench/dynamixel_command', Command)
	# 			print("Requesting position %d at id: %d")%(position, DynaID)
	# 			resp1 = dyna_call(command,DynaID,addr_name,position)
			
	# 		except rospy.ServiceException, e:
	# 			print("Service Call Failed: %s")%e
		
	# 	def readDyna(self,):
	# 		rospy.Subscriber("/dynamixel_workbench/dynamixel_state",DynamixelStateList, self.DynaPos)		
			
		
	# 	def DynaPos(self,data):
	# 		#print("DynaID: %d is at position: %d")%(data.dynamixel_state[0].id,data.dynamixel_state[0].present_position)
	# 		#print("DynaID: %d is at position: %d")%(data.dynamixel_state[1].id,data.dynamixel_state[1].present_position)
	# 		dyna0 = [data.dynamixel_state[0].id,data.dynamixel_state[0].present_position]
	# 		dyna1 = [data.dynamixel_state[1].id,data.dynamixel_state[1].present_position]
	# 		self.dyna0 = dyna0[1]		
	# 		self.dyna1 = dyna1[1]
			
	# 	def change34(self):
	# 		os.system("rosnode kill dynamixel_workbench")
	# 		os.system("roslaunch dynamixel_workbench_controllers dynamixel_controllers2.launch")

	# 	def change12(self):
	# 		os.system("rosnode kill dynamixel_workbench")
	# 		os.system("roslaunch dynamixel_workbench_controllers dynamixel_controllers.launch")

	# 	def change5(self):
	# 		os.system("rosnode kill dynamixel_workbench")
	# 		os.system("roslaunch dynamixel_workbench_controllers dynamixel_controllers3.launch")











