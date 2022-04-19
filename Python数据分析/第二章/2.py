import pandas as pd
import sys
import re

url = "https://www.kylc.com/stats/global/yearly_overview/g_gdp.html"
df = pd.read_html(url)[0]
df = pd.DataFrame(df)

# 删除重复的广告行，删除行操作
df = df.drop_duplicates(subset=None, keep=False, inplace=False)

# 检查缺失数据
# 如果你要检查每列缺失数据的数量，使用下列代码是最快的方法。
# 可以让你更好地了解哪些列缺失的数据更多，从而确定怎么进行下一步的数据清洗和分析操作。

# df.isnull().sum().sort_values(ascending=False)

# 删除空值
df = df.dropna()
df = df.reset_index()  # 重新索引

df["GDP(美元$)"] = df["GDP(美元)"]  # 新增一列，等于 列"GDP(美元)"

for i in range(0, 193):
    if str(df["GDP(美元$)"][i]).find("(") >= 0:
        df["GDP(美元$)"][i] = str(re.findall("\((.*)\)", df["GDP(美元$)"][i]))  # 正则表达式
    else:
        df["GDP(美元$)"][i] = str(df["GDP(美元$)"][i]).replace(",", "")

# 替换其中的符号
for i in range(0, 193):
    df["GDP(美元$)"][i] = df["GDP(美元$)"][i].replace(",", "").replace("\"", "").replace("[", "").replace("]", "").replace(
        "'", "")

# 转化为float数据类型
df["GDP(美元$)"] = df["GDP(美元$)"].astype(float)

df = df.loc[:, ["index", "国家/地区", "所在洲", "年份", "GDP(美元$)"]]

# 将object转化为datetime
df.loc[:, "年份"] = pd.to_datetime(df.loc[:, "年份"], format="%Y", errors="coerce")
df.loc[:, "年份"] = df.loc[:, "年份"].dt.strftime("%y")

# 重命名列名称
colNameDict = {"GDP(美元$)": "GDP(美元)"}  # 将"源数据列名"改为"新列名"
df.rename(columns=colNameDict, inplace=True)

print(df.info())
print(df)
