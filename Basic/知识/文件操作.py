# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 17:18:12 2021

@author: Domenic
"""

f = open("../data/data.txt", mode="w", encoding="UTF-8")  # r+ 表示能读也能写，还有 w+ 和 a+


"""
读取
"""
data = f.read()              # 把内容读入内存

data = f.readline()          # 就读一行

data = f.readlines()         # 一行行读入，存入列表（换行符也会读入）


"""
写入
"""
f.write("hhhhhh")            # mode是a的时候，是append，只能追加到最后
                             # mode是w的时候，是write，写入东西就覆盖了原来的所有内容


"""
操作
"""
f.tell()                     # 获取光标位置
f.seek()                     # 移动光标到指定位置，传入参数为位置（比如：100）
f.close()                    # 关闭文件


"""
修改
"""
f.truncate(100)              # 截断文件，传入的参数是光标位置（从100开始，把后面的内容全部删除）
f.seek(0)
f.truncate()  # 这个就相当于清空文件

data.replace("张三", "李四")  # 用 李四 来替换 张三
