# coding = utf-8

"""
you need python
1，分别得到三个单词
2，从左到右顺序，隔一取一
3，从右到左，隔一取一
4，字符串反序
"""

a = 'you need python'

print(a[0:3], "\n", a[4:8], '\n', a[-6:])    # 不好
print(a.split())

print(a[::2])
print(a[::-2])
print(a[::-1])

