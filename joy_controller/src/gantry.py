import serial
import time

class Gantry:
	#x_axis = serial.Serial('/dev/ttyXGantry',9600)
	y_axis = serial.Serial('/dev/ttyYGantry',9600)
	def __init__(self):

 		#self.x_axis.write(str.encode("\x03"))
		self.y_axis.write(str.encode("\x03"))
		time.sleep(2)
		#self.x_axis.write(str.encode("ex 1\r"))
		self.y_axis.write(str.encode("ex 1\r"))
		time.sleep(3)


	def move_x(self,pos):
		#self.x_axis.write(('r3='+str(int(pos*10))+'\rex 200\r').encode())
		pass

	def move_y(self,pos):
                self.y_axis.write(('r3='+str(int(pos*10))+'\rex 200\r').encode())

	def move(self, x=None, y=None):
                if x > 100:
                        x = 100
                if x < 0:
                        x = 0
                if y > 100:
                        y = 100
                if y < 0:
                        y = 0
                # rospy.loginfo("x:  %f", x)
                # rospy.loginfo("y:  %f", y)		
                if x is not None:
                        self.move_x(x)
                if y is not None:
                        self.move_y(y)
