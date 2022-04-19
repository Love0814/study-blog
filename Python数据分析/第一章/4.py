import datetime

now = datetime.datetime.now()

print("时间格式为：", now.strftime("%Y/%m/%d %H:%M:%S"))
print("时间格式为：", now.strftime("%Y/%m/%d"))

print("年为：", now.year)
print("月为：", now.month)
print("日为：", now.day)
print("小时为：", now.hour)
print("分钟为：", now.second)

print("当前日期为：", now.date())
print("当前时间为：", now.time())

print("返回struct_time为", now.timetuple())
print("返回UTC的struct_time为", now.utctimetuple())

print("返回的公历序列数为：", now.toordinal())
print("返回标准日期格式为：", now.isoformat())

print("返回的周几（1表示周一）", now.isoweekday())
print("返回的周几（0表示周一）", now.weekday())

print(datetime.datetime.strptime("2021/10/30 8:8:00", "%Y/%m/%d %H:%M:%S"))
