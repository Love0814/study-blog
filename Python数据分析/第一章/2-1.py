# 计算cos^3 x+sin^3 x 的最大值最小值

import matplotlib.pyplot as plt
import numpy as np
import math

pi = math.pi
x = np.linspace(0, 12*pi, 1000)
y = (np.cos(x))**3 + (np.sin(x))**3

print(plt.figure())
print(plt.plot(x, y))
print(plt.show())
