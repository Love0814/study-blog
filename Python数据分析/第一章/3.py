import pdfplumber
import os

with pdfplumber.open(r"/Users/cuihao1/本地文件/数据分析/08 专题七  Python数据分析/专题七数据文件/1、Python入门数据文件/平安银行：2020年年度报告.PDF") as p:
    page_count = len(p.pages)
    for i in range(0, page_count):
        page = p.pages[i]
        textdata = page.extract_text()
        data = open("/Users/cuihao1/本地文件/数据分析/08 专题七  Python数据分析/专题七数据文件/1、Python入门数据文件/平安银行：2020年年度报告.txt", "a", encoding="utf-8")
        data.write(str(textdata))

print(page_count)
