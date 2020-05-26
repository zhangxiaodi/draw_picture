# show the attention model influence in our proposed model
import matplotlib.pyplot as plt

x_data=[1,2,3,4,5]#假定的X轴数据

y1_data=[x**2 for x in x_data]#假定Y轴数据是X轴数据的平方

y2_data=[x**3 for x in x_data]#假定Y轴数据是X轴数据的立方

l1, = plt.plot(x_data,y1_data,label='our')#将平方数据展示在图上
l2, = plt.plot(x_data,y2_data,label='baseline')#将立方数据展示在图上

plt.xlabel('x_label')#设置x轴的标签为x_label

plt.ylabel('y_label')#设置x轴的标签为x_label

plt.title('lineplot example')#设置图表标题

plt.legend()#设置图例的前题是l1,l2指定了label
plt.savefig('./test.jpg')
plt.show()





# https://matplotlib.org/gallery/index.html