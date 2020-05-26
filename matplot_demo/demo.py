import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import matplotlib.finance as mpf


fig = plt.figure(figsize=(10,8))

ax1 = fig.add_subplot(321)
plt.title('hello')
ax2 = fig.add_subplot(3,2,2)

ax3 = fig.add_subplot(3,2,3)

ax4 = fig.add_subplot(3,2,4)

ax5 = fig.add_subplot(3,2,5)

ax6 = fig.add_subplot(3,2,6)

data1 = np.random.randn(20)
x = np.arange(20)


ax1.plot(data1)  # 折线图
ax2.scatter(data1,data1,color='r')  # 折线图
ax3.hist(data1, bins=10, alpha=0.3)  # 直方图
ax4.bar(x, data1)  # 柱状图
ax5.pie(np.random.randint(1,15,5), explode=[0, 0, 0.2, 0, 0])  # 饼形图
ax6.plot(x, data1, color='green')  # 组合图
ax6.bar(x, data1, color='k')

fig, axes = plt.subplots(3,3,figsize=(20,16))
data2 = DataFrame(np.random.randn(10,5), columns=['A','B','C','D','E'], index = np.arange(0,100,10))

data2.plot(kind='line', ax=axes[0][0])  # 折线图
data2.plot(kind='scatter', x=data2.index[0], y=data2.index[0],ax=axes[0][1]) # 作散点图
data2.plot(kind='hist', ax=axes[0][2], legend=False)  #作直方图
data2.plot(kind='bar', ax=axes[1][0]) # 作柱状图
data2.plot(kind='area', ax=axes[1][1], stacked = False) # 面积图

train_data = np.array(data2)
mpf.candlestick_ohlc(axes[1][2], train_data.tolist(), width=1.5, colorup='r', colordown='g') #K线图

axim = axes[2][0].imshow(data2.values, interpolation='nearest') # 热力图
plt.colorbar(axim)

plt.legend(loc = 'best')
plt.title('hello')
plt.show()
print(x)

'''
plt.xlabel('横坐标名称')
plt.title('标题')
plt.xlim([0,20])  #添加x轴范围
ax.set_xyick([0,250,500,750,1000])  #设置x轴标签
ax.text(x,y,'text',family = '',fontsize = '')  #添加文本
plt.setp(ax.get_xticklables(),viseble = False)  #隐藏x轴标签，多图使用
plt.subplot_adjust(left = None,right = None,top = None,wspace = None,hspace = None)  #调整子图间距
plt.axhline(y = 0,linewidth = 1,color = 'green')   #添加分割线
plt.grid(True)   #添加网格
plt.savefig('filepath')  #保存图片
'''