# 字典

import re

stock_dic = {}
f = open("data/stock_data.txt", encoding="utf-8")

# 读取第一列（标题栏）
headers = f.readline().strip().split(",")

for line in f:
    line = line.strip().split(",")
    stock_dic[line[0]] = line
f.close()
# print(stock_dic)
# for i,j in stock_dic.items():
#     print(i,j)

while True:
    cmd = input("请输入要查询的股票指令").strip()
    if not cmd:
        continue
    if cmd == "退出":
        break
    
    for s_id, s_data in stock_dic.items():
        s_name = s_data[1]
        if cmd in s_name:
            print(s_data)
    
    # 判断公式的合法性（正则表达式）
    cmd_parser = re.split("[<>]", cmd)

    if len(cmd_parser) != 2:
        continue

    filter_column, filter_val = cmd_parser

    # 列名是否合法 **当前价、涨跌幅、换手率**
    if filter_column not in ["当前价", "涨跌幅", "涨跌额"]:
        continue
    # 判断数值的合法性
    try:
        filter_val = float(filter_val)
    except ValueError:
        continue


    # 根据列名，拿到要查的列的索引
    column_index = headers.index(filter_column)
    for s_id, s_data in stock_dic.items():
        if ">" in cmd:
            if float(s_data[column_index].strip("%")) > filter_val:
                print(s_data)
        else:
            if float(s_data[column_index].strip("%")) < filter_val:
                print(s_data)
