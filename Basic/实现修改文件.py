# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 20:33:05 2021

@author: Domenic
"""

# 占硬盘方式的文件修改
f_name = "data.txt"
f_new_name = "%s~new.txt" % f"{f_name.split('.')[0]}"

old_str = "张三"    # 原文件中要被替换的字符串
new_str = "张三三"  # 新文件中用来替换的字符串

f = open("data/" + f_name, mode='r', encoding="UTF-8")
f_new = open("data/" + f_new_name, mode='w', encoding="UTF-8")
offset = 0  # 代替f.seek() 来记录读完一行后的光标位置
cnt_row = 1
for line in f:
    if old_str in line:
        print(f"Row {cnt_row}")
        print("Old line: {}".format(line), end='')
        new_line = line.replace(old_str,new_str)
        print("New line: {}".format(new_line))
    else:
        new_line = line
    cnt_row += 1
    offset += len(line)
    f_new.write(new_line)

f.close()
f_new.close()
