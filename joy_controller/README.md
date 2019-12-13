# This is instructions for starting up the Robot Arm Gantry System 

This dynamixel based robot arm uses the dynamixel ROS API to do service calls to the ros systems in which positions are requested
and the dynamixels try to go to that position based off of software limits.

Currently inverse kinematics is not implemented due to the ROS API not being able to handle dynamixels of different protocols daisy
chained together to the U2D2. As such the ROS integration has to be rewritten such that all dynamixels can be controlled

Teleoperation was integrated into the system with the the joy_controller package.

![Image of irl RobotArm](https://github.com/ji81930/Robotic_Arm/blob/master/pictures/robot_arm_gantry.jpg)



Steps to operate the Cartesian Robot/Cobra:
1. Move the linear positioner directly attached to the arm to its farthest point.
2. Flip the battery bank power switch to turn on the Pi
3. Ensure that the emergency stop button is released to power on the system
4. Connect to UbiquityRobots**** Wi-Fi network
5. $ssh ubuntu@ubiquityrobot.local
6. Password: ubuntu
7. Launch the robot Arm in ROS:
  a. roslaunch joy_controller cart_control.launch
  
  
  
 
