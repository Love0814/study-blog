# coding= utf-8

import numpy as np
print(np.__version__)

a = np.array([1, 2, 3, 4])      # 1*4矩阵
b = np.array([[1, 2], [3, 4]])      # 2*2矩阵
print(a)
print(b)

x1 = np.arange(30).reshape(2, 3, 5)     # 2个3*5矩阵
x2 = np.arange(30).reshape(3, 5, 2)     # 3个5*2矩阵
print(x1)
print(x2)

s = np.zeros(4)
print(s)

x = np.arange(9)
print(x[3:7])

y = np.arange(12)
print(y)
print(y[3:7])
print(y[0:9:2])
print(y[::-1])

# 广播机制
np1 = np.arange(3)
print(np1 + 5)

np2 = np.ones([3, 3], dtype=int)
print(np1 + np2)
