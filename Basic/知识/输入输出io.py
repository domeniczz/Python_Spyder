# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 23:11:12 2021

@author: Domenic
"""

"""
输入
"""
# 实现一行输入多个数字，并以空格隔开
b = list(map(int, input(": ").split()))
print(b)

# 实现一行输入多个数字，并以空格隔开
b = list(map(int, input(": ").split(',')))
print(b)

# 实现一行输入多个数字(当作字符串来读取)，并以空格隔开
n = input(": ").split()
print(list(n))
print(tuple(n))


"""
输出
"""
url = "https://www.cnblogs.com/lovejh/p/9201219.html"  # format 教程网址

# 格式化输出 format
val = 10
print(f'I am a {val}')

print('{0} {1} {0}'.format('hello','world'))
# output： hello world hello
print('{a} {tom} {a}'.format(tom='hello',a='world'))
# output： world hello world

# 对齐输出
print('{0:10}|{1:10}|'.format(1, 2))
# output:         1|         2|
print('{0:<10}|{1:>10}|'.format(1, 2))        # < 左对齐，> 右对齐
# output:1         |         2|
print('{0:^10}|{1:^10}|'.format(1, 2))        # ^ 中间对齐
# output:    1     |    2     |
print('{0:^10.2f}|{1:^10.2f}|'.format(1, 2))  # .2f 取小数
# output:   1.00   |   2.00   |

"""
'b' - 二进制
'd' - 十进制
'o' - 八进制
'x' - 十六进制
'c' - 字符
'e' - 幂符号
'g' - 一般格式
'n' - 数字。当值为整数时和'd'相同，值为浮点数时和'g'相同。不同的是它会根据区域设置插入数字分隔符。
'%' - 百分数。将数值乘以100然后以fixed-point('f')格式打印，值后面会有一个百分号。
"""
print('{:10c}|'.format(97))  # 10 是占用 10 个空位
# output:         a|
print('{:10.3%}|'.format(0.5))  # .3 是包含 3 位小数
# output：   50.000%|
