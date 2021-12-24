# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 23:57:29 2021

@author: Domenic

spyder 命令行运行： %run 查找替换.py 张三 张四 data/data.txt
"""

import sys

# argv 是命令行参数
print(sys.argv)
old_str = sys.argv[1]
new_str = sys.argv[2]
filename = sys.argv[3]
# old_str = "张三"
# new_str = "张四"
# filename = "data/data.txt"

# 1 load into ram
f = open(filename, mode="r+", encoding="UTF-8")
data = f.read()

# 2. count and replace
old_str_count = data.count(old_str)
new_data = data.replace(old_str,new_str)
# 3. clear old filename
f.seek(0)
f.truncate()

# 4. save new data into file
f.write(new_data)
f.close()

print(f"成功替换字符 '{old_str}' 为 '{new_str}', 共{old_str_count}处")
