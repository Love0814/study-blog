# coding= utf-8

"""
有如下技术栈名称集合：
skill={"python","R","SQL","Git","Tableau","SAS"}
假定自己的技术是： mySkills = {"python","R"}
-判断自身所掌握技术是否在技术栈范围之内
"""

skills = {'Python', 'R', 'SQL', 'Git', 'Tableau', 'SAS'}
mySkills = {'Python', 'R'}

print(mySkills.issubset(skills))

"""
参考答案：
r = mySkills.intersection(skills)
"""
