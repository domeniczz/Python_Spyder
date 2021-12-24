# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 16:43:21 2021

@author: Domenic
"""

'''
输出：
玩家1的牌为：['方块3', '黑桃A', '方块8']
玩家2的牌为：['方块9', '方块J', '方块10']
玩家3的牌为：['红桃5', '黑桃5', '红桃4']
玩家4的牌为：['红桃8', '红桃A', '梅花K']
玩家5的牌为：['梅花5', '梅花J', '梅花A']
最终排名：	玩家2第一名	玩家4第二名	玩家5第三名	玩家3第四名	玩家1第五名
'''

import random
# import operator

puke = []  # 存储扑克牌
num_list = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
hua_list = ['梅花', '红桃', '黑桃', '方块']
sotr_dic = {'2': 0, '3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6, '9': 7, '10': 8, 'J': 9, 'Q': 10, 'K': 11, 'A': 12,
            '对子': 15, '顺子': 30, '顺金': 60, '豹子': 100}

count_new_list = []  # 存储玩家分数和排序后排名
count_dic = {}  # 存储玩家分数

# 准备52张扑克
for hua in hua_list:
    for num in num_list:
        a = hua + num
        puke.append(a)
player_dic = {'玩家1': [], '玩家2': [], '玩家3': [], '玩家4': [], '玩家5': []}

# 随机给五个玩家发牌
# print(len(puke))
for key, value in player_dic.items():
    for i in range(3):
        plate = random.sample(puke, 3)
        player_dic[key] = plate
        for i in plate:
            puke.remove(i)

# print(player_dic)


# 获取玩家的牌型
def paixing(list1):
    num = []
    huase = []
    for i in list1:
        a = i[2:]
        b = i[:2]
        num.append(a)
        huase.append(b)
    return num, huase


# 对数字的牌型进行排序
def sotr(num):
    new_num = []
    sort_list2 = []
    list1 = []
    for i in num:
        new_num.append(sotr_dic[i])
    new_num = sorted(new_num)
    for new in new_num:
        sort_list2.append([k for k, v in sotr_dic.items() if v == new])
    for m in sort_list2:
        for n in m:
            list1.append(n)
    return list1


# 对玩家的牌形统计分数
def count(num, huase):
    a = 0
    base_count = sotr_dic[num[0]] + sotr_dic[num[1]] + sotr_dic[num[2]]
    if num[0] == num[1] and num[1] == num[2]:
        paixing = '豹子'
        a = base_count + sotr_dic[paixing]
        # print(paixing, a)
    elif (sotr_dic[num[0]] + 1 == sotr_dic[num[1]] and sotr_dic[num[2]] - 1 == sotr_dic[num[1]]) and (huase[0] == huase[
        1] and huase[1] == huase[2]):
        paixing = '顺金'
        a = base_count + sotr_dic[paixing]
        # print(paixing, a)
    elif (sotr_dic[num[0]] + 1 == sotr_dic[num[1]]) and (sotr_dic[num[2]] - 1 == sotr_dic[num[1]]) and (
            huase[0] != huase[
        1] or huase[1] != huase[2]):
        paixing = '顺子'
        a = base_count + sotr_dic[paixing]
        # print(paixing, a)
    elif (num[0] == num[1] and num[1] != num[2]) or (num[1] == num[2] and num[0] != num[1]) or (
            num[0] == num[2] and num[1] != num[0]):
        paixing = '对子'
        a = base_count + sotr_dic[paixing]
        # print(paixing, a)
    else:
        a = base_count
    return a


# 对存储玩家分数的字典进行排序
def compare(count_dic):
    d = list(zip(count_dic.values(), count_dic.keys()))
    return sorted(d, reverse=True)


for key, value in player_dic.items():
    # print(key,value)
    num, huase = paixing(value)
    # print(num,huase)
    num = sotr(num)
    # print(num, huase)
    count1 = count(num, huase)
    # print(count1)
    count_dic[key] = count1
    print(key + "的牌为：" + str(value))
    count_new_list = compare(count_dic)
# print(count_new_list)
print('最终排名：' + "\t" + count_new_list[0][1] + "第一名" + "\t" + count_new_list[1][1] + "第二名" + "\t" + count_new_list[2][
    1] + "第三名" + "\t" + count_new_list[3][1] + "第四名" + "\t" + count_new_list[4][1] + "第五名")
