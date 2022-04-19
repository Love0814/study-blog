from datetime import datetime
from datetime import timedelta

now = datetime.now()
aDay = timedelta(days=1)
tomorrow = now + aDay
print(tomorrow.strftime("%Y-%m-%d"))

yesterday = now - aDay
print(yesterday.strftime("%Y-%m-% d"))
