# coding = utf-8

"""
将字符串 'python' 转化为列表（记为lst），然后完成以下操作
-将字符串 'rust' 中的每个字母作为独立元素追加到lst中
-对lst排序
删除lst中重复元素
"""

lst = list("python")

lst.extend(list("rust"))

lst.sort()

lst.remove("t")

print(lst)
