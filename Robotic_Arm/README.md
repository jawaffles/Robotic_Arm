# Robot Arm Simulation Instructions

## Robot Arm Simple Simulation

To simply launch the Gazebo Simulation of Robot arm 

`roslaunch Robotic_Arm gazebo.launch`

Control of joints can be sent by publishing to the appropriate topic using the ROS control mangaer.

`rostopic pub /Robotic_Arm/arm_joint_1_position_controller/command std_msgs/Float64 "data: 0.0" `



## Robot Arm Moveit IK Implementation

To launch the Robot arm with moveit based control 

`roslaunch Robotic_Arm Robotic_Arm_bringup_moveit.launch`

This ball on the Robot arm can be used to move the end effector and send goals for the Robot Arm


![Image of irl RobotArm](https://github.com/ji81930/Robotic_Arm/blob/master/pictures/MoveitRoboticArm.png)



## Robot IKpy Implementation

IKpy is a lightweight python library that calculates inverse kinematics through import of the URDF. It calculates the Denavit Hardenburg Matrix

Ikpy Can be  used to give coordinate positions and calculate inverse kinematics for joints in the robot (Still experimental, denavit hardenburg matrix from URDF is incorrect, must be recalculated.)

![Image of irl RobotArm](https://github.com/ji81930/Robotic_Arm/blob/master/pictures/ikpy.png)




## Folder Descriptions

A URDF file was generated from solidworks CAD model using the SWtoURDF add in SOlidworks. Significant reconfiguring was needed as the add in still has bugs


In the URDF folder the joints and links are defined for the robot arm for which there are 4 main joints. This URDF also references the CAD files inside the mesh folder for inertial and visual simulation of the Robot arm. 
