import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline

print(tf.__version__)

data = pd.read_csv('./dataset/Income.csv')

print(data)

plt.scatter(data.Education,data.Income)

plt.show()