# coding = utf-8

"""
1，' hello '去除空格
2，'you need python' 用 '*'替代空格
"""

a = ' hello '
print(a.strip())

b = 'you need python'
print(b.replace(' ', '*'))
print('*'.join(b.split()))  # 也可以
