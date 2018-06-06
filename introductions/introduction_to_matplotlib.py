# coding: utf-8

# In[ ]:


import matplotlib.pyplot as plt
import numpy as np

# In[ ]:


data = np.arange(100, 201)
# print(data)
plt.plot(data)
# 通过plt.show()将这个图形显示出来
# plt.show()

data2 = np.arange(200, 301)
# 可以简单的理解为一个figure就是一个图形窗口
# matplotlib.pyplot会有一个默认的figure，我们也可以通过plt.figure()创建更多个
plt.figure()
plt.plot(data2)
plt.show()

# In[ ]:


data = np.arange(100, 201)
# 下面这行代码指的是：2行1列subplot中的第1个subplot
plt.subplot(2, 1, 1)
plt.plot(data)
plt.show()

data2 = np.arange(200, 301)
# 下面这行代码指的是：2行1列subplot中的第2个subplot
plt.subplot(2, 1, 2)
plt.plot(data2)
plt.show()
# subplot函数的参数不仅仅支持上面这种形式，还可以将三个整数（10之内的）合并一个整数
# 例如：2, 1, 1可以写成211，2, 1, 2可以写成212。


# In[ ]:


# plot函数的第一个数组是横轴的值，第二个数组是纵轴的值
# 所以它们一个是直线，一个是折线
# 最后一个参数是由两个字符构成的，分别是线条的样式和颜色
# 前者是红色的直线，后者是绿色的点线。
plt.plot([1, 2, 3], [3, 6, 9], '-r')
plt.plot([1, 2, 3], [2, 4, 9], ':g')

plt.show()

# In[ ]:


# scatter函数用来绘制散点图
N = 20
# 这幅图包含了三组数据，每组数据都包含了20个随机坐标的位置
# 参数c表示点的颜色，s是点的大小，alpha是透明度
plt.scatter(np.random.rand(N) * 100,
            np.random.rand(N) * 100,
            c='r', s=100, alpha=0.5)

plt.scatter(np.random.rand(N) * 100,
            np.random.rand(N) * 100,
            c='g', s=200, alpha=0.5)

plt.scatter(np.random.rand(N) * 100,
            np.random.rand(N) * 100,
            c='b', s=300, alpha=0.5)

plt.show()

# In[ ]:


# pie函数用来绘制饼状图
# 图中的标签通过labels来指定
labels = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
# data是一组包含7个数据的随机数值
data = np.random.rand(7) * 100
# autopct指定了数值的精度格式
plt.pie(data, labels=labels, autopct='%1.1f%%')
# plt.axis('equal')设置了坐标轴大小一致
plt.axis('equal')
# plt.legend()指明要绘制图例（见下图的右上角）
plt.legend()

plt.show()

# In[ ]:


# bar函数用来绘制条形图
N = 7
# 这幅图展示了一组包含7个随机数值的结果，每个数值是[0, 100]的随机数
x = np.arange(N)
data = np.random.randint(low=0, high=100, size=N)
# 它们的颜色也是通过随机数生成的
# np.random.rand(N * 3).reshape(N, -1)表示先生成21（N x 3）个随机数，
# 然后将它们组装成7行，那么每行就是三个数，这对应了颜色的三个组成部分。
colors = np.random.rand(N * 3).reshape(N, -1)
# title指定了图形的标题，labels指定了标签，alpha是透明度

labels = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
plt.title("Weekday Data")
plt.bar(x, data, alpha=0.8, color=colors, tick_label=labels)

plt.show()

# In[ ]:


# hist函数用来绘制直方图,直方图看起来是条形图有些类似
# 但它们的含义是不一样的，直方图描述了数据中某个范围内数据出现的频度

# [np.random.randint(0, n, n) for n in [3000, 4000, 5000]]生成了包含了三个数组的数组
# 这其中： 
# 第一个数组包含了3000个随机数，这些随机数的范围是 [0, 3000)
# 第二个数组包含了4000个随机数，这些随机数的范围是 [0, 4000)
# 第三个数组包含了5000个随机数，这些随机数的范围是 [0, 5000)
data = [np.random.randint(0, n, n) for n in [3000, 4000, 5000]]
# bins数组用来指定我们显示的直方图的边界
# 即：[0, 100) 会有一个数据点，[100, 500)会有一个数据点，以此类推
# 所以最终结果一共会显示7个数据点
# 同样的，指定了标签和图例。
labels = ['3K', '4K', '5K']
bins = [0, 100, 500, 1000, 2000, 3000, 4000, 5000]

plt.hist(data, bins=bins, label=labels)
plt.legend()

plt.show()
