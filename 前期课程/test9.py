# coding = utf-8

"""
编写程序，判断用户输入的数字是奇数还是偶数
"""
"""
num = input("请输入您喜欢的数字：")

num = int(num)

num_ys = num % 2
if num_ys == 0:
    print("您输入的是偶数")
else:
    print("您输入的是奇数")
"""

n = input("请输入一个自然数：")
if n.isdigit():
    n = int(n)
    if n % 2 == 0:
        print("{0}是一个偶数。".format(n))
    else:
        print("{0}是一个奇数。".format(n))
else:
    print("请输入一个自然数。")
