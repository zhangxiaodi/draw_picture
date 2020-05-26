import numpy as np
import matplotlib.pyplot as plt

length = 14
x_label = np.array(length)
ours = (0.2900,0.2447,0.3600,0.6735,0.5464,0.4375,0.5100,0.5400,0.2700,0.6700,	0.8105,	0.5300,	0.2700,	0.5900)
baseline = (0.1700,0.1489,0.0900,0.5408,0.1649,0.2083,0.0700,0.3000,0.2000,0.6100,0.6105,0.2900,0.1500,0.3400)



ours_angle = (26.6473,18.6253,3.8226,4.3286,7.4451,30.0128,4.3384,5.3031,8.3008,6.7496,7.1308,3.4740,17.7902,16.2228)
baseline_angle = (37.4622,66.1088,17.7650,8.0102,19.0118,39.5476,22.8348,7.3378,12.9637,6.9907,11.1714,14.0034,43.305,37.163)


mean_pro_our = np.mean(ours)
mean_pro_baseline = np.mean(baseline)
mean_angle_our = np.mean(ours_angle)
mean_angle_baseline = np.mean(baseline_angle)

# our_data = (5.44,2.67,3.44,5.84,2.58,4.26,6.44,3.19,2.6,4.7,5.1,4,5.8) #np.random.randint(1,100,13)#假定Y轴数据是X轴数据的平方

# baseline_data =  (6.06,3.29,4.58,3.37,5.31,6.28,9.72,5.32,6.20,5.71,7.13,4.91,7.81)#np.random.randint(1,50,13)#假定Y轴数据是X轴数据的立方


ind = np.arange(len(ours))  # the x locations for the groups
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind - width / 2, ours, width, color='SkyBlue', label='ours')
rects2 = ax.bar(ind + width / 2, baseline, width, color='IndianRed', label='baseline')

x_ticks = ('1','2','3','4','5','6','7','8',
          '9','10','11','12','13','14')
# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('5px 2D Projection', fontsize=25)
ax.set_title('Projection accuracy in RU-APC dataset', fontsize=25)
ax.set_xlabel('3D object', fontsize=25)
#plt.xlabel('3D object', fontsize=25)#设置x轴的标签为x_label

#plt.ylabel('Angle error',fontsize=25)#设置x轴的标签为x_label

#plt.title('Angle error in dataset', fontsize=32)#设置图表标题

plt.xticks(ind, x_ticks)
ax.legend()

plt.show()

