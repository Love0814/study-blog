# coding = utf-8

"""
找出以下两个字典共有的键：
{'a':1, 'b':2, 'c':3, 'd':4}
{'b':22, 'd':44, 'e':55, 'f':77}
"""

dict1 = dict(a=1, b=2, c=3, d=4)
dict2 = dict(b=22, d=44, e=55, f=77)

dict1_set = set(dict1.keys())
dict2_set = set(dict2.keys())

c = dict1_set.intersection(dict2_set)

dict_c = c

print(dict_c)

d = dict1.keys() & dict2.keys()

print(d)
