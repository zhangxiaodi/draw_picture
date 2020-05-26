import matplotlib.pyplot as plt
import numpy as np

x = [1,2,3,4,5,6,7,8,9,10,11,12,13]
x = np.array(x)
x_data = ['Ape','Benchvise','Cam','Can','Cat','Driller','Duck','Eggbox',
          'Glue','Holcpuncher','Iron','Lamp','Phone']#假定的X轴数据

y1_data = [5.44,2.67,3.44,5.84,2.58,4.26,6.44,3.19,2.6,4.7,5.1,4,5.8] #np.random.randint(1,100,13)#假定Y轴数据是X轴数据的平方

y2_data =  [6.06,3.29,4.58,3.37,5.31,6.28,9.72,5.32,6.20,5.71,7.13,4.91,7.81]#np.random.randint(1,50,13)#假定Y轴数据是X轴数据的立方

our_mean = np.mean(y1_data)
baseline_mean = np.mean(y2_data)
#l1 = plt.plot(x_data,y1_data,label='baseline')#将平方数据展示在图上
#l2 = plt.plot(x_data,y2_data,label='ours')#将立方数据展示在图上

print(our_mean)
print(baseline_mean)

plt.xticks(x, x_data)
plt.bar(x - 0.3/2, y1_data, width=0.3, color='red',  tick_label=x_data, edgecolor='red', label='oures', lw=3)
plt.bar(x + 0.3/2, y2_data, width=0.3, color='green',  tick_label=x_data, edgecolor='green', label='baseline', lw=3)


plt.xticks(fontsize=14)
plt.yticks(fontsize=18)

plt.xlabel('3D object', fontsize=25)#设置x轴的标签为x_label

plt.ylabel('Angle error',fontsize=25)#设置x轴的标签为x_label

plt.title('Angle error in dataset', fontsize=32)#设置图表标题

font = {
         'size': 53,
         }
plt.legend()#设置图例的前题是l1,l2指定了label

plt.show()