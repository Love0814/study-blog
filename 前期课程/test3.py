# coding = etf-8

'''
变长3，7，9 计算三个角度数（弧度制表示）
'''
import fractions
import math
from fractions import Fraction

x = 3
y = 7
z = 9

a = round(
    math.degrees(
        math.acos(
            Fraction(y ** 2 + z ** 2 - x ** 2, 2 * y * z)
        )
    ), 2
)

b = round(
    math.degrees(
        math.acos(
            Fraction(x ** 2 + z ** 2 - y ** 2, 2 * x * z)
        )
    ), 2
)

c = round(
    math.degrees(
        math.acos(
            Fraction(x ** 2 + y ** 2 - z ** 2, 2 * x * y)
        )
    ), 2
)
print("角1=", a, "度","角2=", b, "度","角3=", c, "度")


