import matplotlib.pyplot as plt

x_data=[1,2,3,4,5,6,7]#假定的X轴数据

#y1_data=[x**2 for x in x_data]#假定Y轴数据是X轴数据的平方
y1_data = [92.76, 94.38, 95.57, 96.5, 96.7, 96.6, 96.7]
#y2_data=[x**3 for x in x_data]#假定Y轴数据是X轴数据的立方

l1, = plt.plot(x_data,y1_data,color='red')#将平方数据展示在图上
#l2, = plt.plot(x_data,y2_data,label='cubic')#将立方数据展示在图上

plt.xlabel('The numbers of feature pyramid')#设置x轴的标签为x_label

plt.ylabel('accuracy')#设置x轴的标签为x_label

plt.title('The influence of pyramid number')#设置图表标题

plt.legend()#设置图例的前题是l1,l2指定了label

plt.show()