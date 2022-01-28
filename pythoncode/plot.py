import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
 
# np.random.seed(1)
# x=np.random.rand(10)
# print(x)
# y=np.random.rand(10)
 
# colors=np.random.rand(10)
# area=(30*np.random.rand(10))**2
 
# plt.plot(x,y,s=area,c=colors,alpha=0.5)
# plt.show()


# a = np.arange(12).reshape(2,6)
 
# print ('原数组：')
# print (a)
# print ('\n')
 
# print ('转置数组：')
# print (a.T)

# a = np.array([0,30,45,60,90])  
# print ('含有正弦值的数组：')
# sin = np.sin(a*np.pi/180)
# plt.plot(sin)

a = ["Google", "Runoob", "Wiki"]

myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar)

testvar = pd.Series(index=range(5,8), range(1,4))

print(testvar)






