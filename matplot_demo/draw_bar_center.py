import numpy as np
import matplotlib.pyplot as plt

men_means = (20, 35, 30, 35, 27)
women_means = (25, 32, 34, 20, 25)


our_data = (5.44,2.67,3.44,5.84,2.58,4.26,6.44,3.19,2.6,4.7,5.1,4,5.8) #np.random.randint(1,100,13)#假定Y轴数据是X轴数据的平方

baseline_data =  (6.06,3.29,4.58,3.37,5.31,6.28,9.72,5.32,6.20,5.71,7.13,4.91,7.81)#np.random.randint(1,50,13)#假定Y轴数据是X轴数据的立方


ind = np.arange(len(our_data))  # the x locations for the groups
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind - width / 2, our_data, width, color='SkyBlue', label='ours')
rects2 = ax.bar(ind + width / 2, baseline_data, width, color='IndianRed', label='baseline')

x_ticks = ('Ape','Benchvise','Cam','Can','Cat','Driller','Duck','Eggbox',
          'Glue','Holcpuncher','Iron','Lamp','Phone')
# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Mean angle error', fontsize=25)
ax.set_title('Angle error in dataset', fontsize=25)
ax.set_xlabel('3D object', fontsize=25)
#plt.xlabel('3D object', fontsize=25)#设置x轴的标签为x_label

#plt.ylabel('Angle error',fontsize=25)#设置x轴的标签为x_label

#plt.title('Angle error in dataset', fontsize=32)#设置图表标题

plt.xticks(ind, x_ticks)
ax.legend()

plt.show()
