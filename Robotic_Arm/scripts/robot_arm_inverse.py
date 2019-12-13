import ikpy 
import numpy as np
from ikpy import plot_utils
import matplotlib.pyplot as plt
import matplotlib
from ipywidgets import interact, FloatSlider

from mpl_toolkits.mplot3d import Axes3D
ax = matplotlib.pyplot.figure().add_subplot(111, projection='3d')

my_chain = ikpy.chain.Chain.from_urdf_file("/home/biosensing/catkin_ws/src/Robotic_Arm/urdf/Robotic_Arm.urdf", base_elements=None, last_link_vector=None, base_element_type='link', active_links_mask=None, name='chain')


my_chain.active_links_mask[True,True,True,True,True]
# my_chain.active_links_mask




test = my_chain.inverse_kinematics([
    [1, 0, 0, .5],
    [0, 1, 0, 0],
    [0, 0, 1, .5],
    [0, 0, 0, 1]
    ])

print(test)

my_chain.plot(test, ax)
matplotlib.pyplot.show()


# print("The angles of each joints are : ", my_chain.inverse_kinematics(target_frame))



# ax = plot_utils.init_3d_figure()

# plt.show()


print("Test Complete")


# target_vector = [ 0.1, -0.2, 0.1]
# target_frame = np.eye(4)
# target_frame[:3, 3] = target_vector


#my_chain.plot(my_chain.inverse_kinematics(target_frame), ax, target=target_vector)
# plt.xlim(-0.1, 0.1)
# plt.ylim(-0.1, 0.1)




