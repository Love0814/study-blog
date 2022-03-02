# coding = utf-8
"""
编写程序，判断用户输入的网址主域名是否符合规定的格式要求。
-网站主域名格式：www.xxxx.xxx
"""
"""
ads = input("请输入您要查询的网站：")

web = ads.split(".")

print(web)
"""

domain = input("please input a domain name:")

postfix = ("com", "net", "cn")

lst = domain.split(".")

if (len(lst) < 2) or (len(lst) > 4):
    print("sorry! your domain is not right.")
elif lst[-1] not in postfix:
    print("The domain does not cpmply with the regulations.")
else:
    print("The domain is right.")
