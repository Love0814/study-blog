"""
询问用户姓名和年龄
计算十年后的年龄
打印用户的姓名，以及现在和10年后的年龄
"""

name = input('请输入您的姓名：')
age = input('请输入您的年龄：')

age2 = int(age) + 10

print(' 您的姓名是：', name, '\n', '您的年龄是：', age, '岁', '\n', '您十年后的年龄是：', age2, '岁')

"""
参考答案：

name = input('your name:')
age = input('your age:')

after_ten = int(age) + 10

print('-' * 10)
print('your name is {0}. \nyou are {1} years,now. \nAfter ten years, you are {2}'.format(name, age, after_ten))
"""
