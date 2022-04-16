# coding = utf-8

"""
判断用户的键盘输入内容：
- 如果都是数字，则将该数字扩大10倍，然后打印显示。
- 如果是字母，则在其后面增加"@python"后打印显示。
- 其他情况则将输入的内容按原样显示。
"""

i = input("请输入您的内容：")

if i.isalnum():
    if i.isdigit():
        print("您输入的是数字，它的十倍是：", int(i) * 10)
    elif i.isalpha():
        print("您输入的是字母，", i, "@python")
    else:
        print(i)
else:
    print(i)
