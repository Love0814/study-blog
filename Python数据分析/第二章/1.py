import pandas as pd

res = pd.Series([2, 5, 8, 12, 17], index=["A", "B", "C", "D", "E"])
print(res)
print("索引：", res.index)
print("数组：", res.values)

df = pd.DataFrame({"X": ["a", "b", "c"], "Y": range(10, 13), "Z": [4, 5, 6]})
print(df)

print(df.loc[:, ["Y"]])  # 选取某一列
print(df[["X", "Y"]])  # 选取多列
print(df.iloc[:, [0, 1]])  # 选取多列

print(df.loc[1, :])  # 选取某一行
print(df.loc[[0, 1], :])  # 选取多行
print(df.iloc[[0, 1], :])  # 选取多行

print(df.loc[1, "Y"])  # 选取某个元素
print(df.loc[[1], ["Y"]])  # 选取某个元素
print(df.iloc[1, 1])  # 选取某个元素

print(df[df.Y >= 11])   # 单条件筛选
