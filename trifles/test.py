# def inputInt(content = None):
#     while True:
#         data = input(content)
#         try:
#             inputData = eval(data)
#             if type(inputData) == int:
#                 # break
#                 return inputData
#         except:
#             pass
#
# a = inputInt(": ")
# print(a)
# for i in a:
#     print(i)
# import ast

# # need = ast.literal_eval(input("要下载哪些歌（输入序列号）："))
# s = input("输入：").split(' ')

# print(s)
# s = list(map(int, s))

# print(s)

import random
puke = ['梅花2', '红桃2', '黑桃2', '方块2', '梅花3', '红桃3', '黑桃3', '方块3', '梅花4', '红桃4', '黑桃4', '方块4', '梅花5', '红桃5', '黑桃5', '方块5', '梅花6', '红桃6', '黑桃6', '方块6', '梅花7', '红桃7', '黑桃7', '方块7', '梅花8', '红桃8', '黑桃8', '方块8', '梅花9', '红桃9', '黑桃9', '方块9', '梅花10', '红桃10', '黑桃10', '方块10', '梅花J', '红桃J', '黑桃J', '方块J', '梅花Q', '红桃Q', '黑桃Q', '方块Q', '梅花K', '红桃K', '黑桃K', '方块K', '梅花A', '红桃A', '黑桃A', '方块A']
print(random.sample(puke, 3))
