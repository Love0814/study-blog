import pandas as pd

data = pd.read_csv("/Users/cuihao1/本地文件/数据分析/08 专题七  Python数据分析/专题七数据文件/2、pandas数据文件/Pandas入门：Fortune500_2020.csv")

# 描述数据类型
print(data.info())
print(data.describe())
print(data.shape)
print(data.axes)
print(data.columns)
print(data.head())

# 数据选取
print(data.loc[[1, 10], :])
print(data[["Company", "Revenue"]])

# 数据透视表操作
print(data.sort_values(["Revenue", "Profit"], ascending=False))   # 按照收入进行排序

print(pd.pivot_table(data, index=["Industry"], values="Revenue"))   # 按照行业进行数据透视表汇总操作
print(pd.pivot_table(data, index=["Country"], values="Revenue"))    # 按照国家进行数据透视表汇总操作

print(pd.pivot_table(data, index=["Industry"], columns="Country", values="Revenue"))    # 按照国家行业进行分析

# 按照国家统计企业数量
Country_count = data.set_index(["Country", "Profit", "CEO", "Employee", "Industry", "Revenue"]).count(level="Country").sort_values(by="Company", ascending=False)
print(Country_count)
