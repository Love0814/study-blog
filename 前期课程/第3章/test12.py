# coding = utf-8

"""
统计如下字符串中每个单词的数量：
song = "When I am down and oh my soul so weary When troubles
come and my heart burdened be Then I am still and wait here in the
silence Until you come and sit awhile with me You raise me up so I
can stand on mountains You raise me up to walk on stormy seas I
am strong when I am on your shoulders You raise me up to more
than I can be You raise me up so I can stand on mountains You raise
me up to walk on stormy seas I am strong when I am on your
shoulders You raise me up to more than I can be You raise me up so I
can stand on mountains"
"""

song = "When I am down and oh my soul so weary When troubles come and my heart burdened be Then I am still and wait here in the silence Until you come and sit awhile with me You raise me up so I can stand on mountains You raise me up to walk on stormy seas I am strong when I am on your shoulders You raise me up to more than I can be You raise me up so I can stand on mountains You raise me up to walk on stormy seas I am strong when I am on your shoulders You raise me up to more than I can be You raise me up so I can stand on mountains"

words = song.split()
dic = {}

for i in words:
    i = i.lower()
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

print(dic)
