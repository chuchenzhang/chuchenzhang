# 一元函数线性回归
# 单变量的线性方程可以表示为：
# y = w*x + b
# 生成人工数据集，随机生成一个近似采样随机分布，使得w=2.0, b=1，并加入一个振幅为0.4的噪声

import os
import sys

os.environ["TF_CPP_MIN_LOG_LEVEL"] = '2' # 只显示 warning 和 Error 

#在Jupter notebook中，使用matplotlib显示图像需要设置为inline
# %matplotlib inline

import tensorflow as tf #载入库函数 tensorflow 
import numpy as np#numpy 
import matplotlib.pyplot as plt   #matplotlib.pyplot

###########1.准备数据#################
#设置随机数种子
np.random.seed(5)

#直接采用np生成等差数列的方法，生成100个（-1，1）点
x_data=np.linspace(-1,1,100)

#y=2x+1+噪声
y_data=2*x_data+1.0+np.random.randn(*x_data.shape)*0.4

# 显示散点
plt.scatter(x_data,y_data)
# 显示直线
plt.plot(x_data,2*x_data+1.0,color='red',linewidth=3)

# plt.show()
# sys.exit(0)
############数据准备结束##################



###########2.构建模型#############

#定义训练数据的占位符，x为特征值（变量），y是标签值（函数值）
tf.compat.v1.disable_eager_execution()#用tf.compat.v1.来兼容tensorflow版本1的方法。
x=tf.compat.v1.placeholder("float",name="x")
y=tf.compat.v1.placeholder("float",name="y")
#定义模型函数
def model(x,w,b):
    return tf.multiply(x,w)+b

#构建线性函数的斜率和截距，都为变量，tf.Variable为变量声明函数
w=tf.Variable(1.0,name="w0")
b=tf.Variable(0.0,name="b0")

#预测值，向前计算
pred=model(x,w,b)

print(pred)
sys.exit(0)

###########模型构建结束#############



###########3.训练模型##############

#设置训练参数：迭代次数、学习率
train_epochs=10
learning_rate=0.05

#采用均方差为损失函数
loss_function=tf.reduce_mean(tf.square(y-pred))
#定义优化器Optimizer
optimizer=tf.compat.v1.train.GradientDescentOptimizer(learning_rate).minimize(loss_function)

#声明会话
sess=tf.compat.v1.Session()
#变量初始化
init=tf.compat.v1.global_variables_initializer()
sess.run(init)

#开始学习
for epoch in range(train_epochs):
    for xs,ys in zip(x_data,y_data):
        _,loss=sess.run([optimizer,loss_function],feed_dict={x:xs,y:ys})
        b0temp=b.eval(session=sess)
        w0temp=w.eval(session=sess)
        plt.plot(x_data,w0temp*x_data+b0temp)
print("w:",sess.run(w))
print("b:",sess.run(b))


############模型训练结束#############



############4.结果可视化#############

plt.scatter(x_data,y_data,label='Original data')
plt.plot(x_data,x_data*sess.run(w)+sess.run(b),\
        label='Fitted line',color='r',linewidth=3)
plt.legend(loc=2)#通过参数loc指定图例的位置

############结果可视化结束############






############5.利用模型进行预测########

x_test=3.21

predict=sess.run(pred,feed_dict={x:x_test})
print("预测值：%f"%predict)
target=2*x_test+1
print("目标值：%f"%target)

#############预测结束####################




