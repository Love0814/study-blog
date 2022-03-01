# coding = utf-8

"""
通过键盘输入数字，作为圆的半径
计算圆的周长和面积，并分别打印显示出来，结果保留两位小数
"""

import math

c1 = float(input('请输入半径长度：'))
print(' 周长为：', round(2 * c1 * math.pi, 2), '\n', '面积为:', round(2 * math.pi * c1 ** 2, 2))

"""
参考答案：

import math

n = input('please input a number:')  # input输入的是字符串 不是数字 优化可以添加判断是否为数字语句

n = float(n)

circle = 2 * math.pi * n
area = math.pi * n**2

print('the circle is:', round(circle, 2))
print('the area is:', round(area, 2))
"""
