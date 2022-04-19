import pandas as pd
import numpy as np

s = pd.Series(["A", "B", "C", "bbhello", "123", np.nan, "hj"])
df = pd.DataFrame({"key1": list("abcdef"), "key2": ["hee", "fv", "w", "hija", "123", np.nan]})

# 直接通过.str调用字符串方法
# 可以对Series、Dataframe使用
# 自动过滤NaN值
print(s.str.count("b"))

print(df["key2"].str.upper())

# df.columns是一个index对象，也可使用.str
df.columns = df.columns.str.upper()
print(df)
