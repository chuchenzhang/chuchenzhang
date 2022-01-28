import tensorflow as tf

data = tf.constant([1,2])

#使用tensorflow读入一个序列后将其打印
# print(data)	# 具体数直为[1,2]，维度大小为2，数据类型为int32

#打印具体数值
print(data.numpy())