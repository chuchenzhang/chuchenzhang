import tensorflow as tf
import os

# os.environ["TF_CPP_MIN_LOG_LEVEL"] = '1' # 默认，显示所有信息 
os.environ["TF_CPP_MIN_LOG_LEVEL"] = '2' # 只显示 warning 和 Error 
# os.environ["TF_CPP_MIN_LOG_LEVEL"] = '3' # 只显示 Error


vector = tf.constant([4,5,6], dtype=tf.float32)
eucNorm = tf.norm(vector, ord=2) # 求解L2范数，即欧几里得范数，即向量个元素平方之和再开方

print(eucNorm)

print(eucNorm.numpy())







