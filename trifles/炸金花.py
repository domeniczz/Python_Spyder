# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 14:17:54 2021

@author: Domenic
"""

'''
步骤：
1. 发牌
2. 对玩家的牌进行排序
3. 计算玩家牌的大小
4. 选出最大
'''

import random

number_list = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
huase_list = ['梅花', '红桃', '黑桃', '方块']

puke = []
# 5个玩家
player_puke_dic = {'1号': [], '2号': [], '3号': [], '4号': [], '5号': []}

# 牌对应的值
sotr_dic = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13,
            'A': 14}

# 记录每个玩家的
score_dic = {'1号': [], '2号': [], '3号': [], '4号': [], '5号': []}


# 生成扑克牌
def generate_puke():
    for num in number_list:
        for huase in huase_list:
            puke.append(huase + num)
    # print(puke)


# 发牌
def deal():
    generate_puke()
    for player, val in player_puke_dic.items():
        player_puke_dic[player] = random.sample(puke, 3)
    # print(player_puke_dic)
    '''
    {'1号': ['梅花7', '梅花9', '方块K'], 
     '2号': ['黑桃K', '方块6', '方块A'], 
     '3号': ['红桃5', '梅花10', '方块A'], 
     '4号': ['梅花A', '梅花8', '红桃K'], 
     '5号': ['梅花A', '方块6', '黑桃4']}
    '''


# 冒泡排序，降序
def sort_list(cards):
    # cards = ['方块7', '红桃2', '黑桃5']
    for i in range(len(cards)):
        for j in range(len(cards)-1-i):
            if sotr_dic[cards[j][2:]] < sotr_dic[cards[j+1][2:]]:
                tmp = cards[j]
                cards[j] = cards[j+1]
                cards[j+1] = tmp


# 给每个人的牌进行排序（降序）
def sort_player_puke():
    for player, cards in player_puke_dic.items():
        tmp = []
        sort_list(cards)  # 降序排序
        for each in cards:
            # print(player, each[2:])
            tmp.append([each[:2], sotr_dic[each[2:]]])
        player_puke_dic[player] = tmp
        # print(player, player_puke_dic[player])
        '''
        1号 [['梅花', 6], ['方块', 5], ['梅花', 2]]
        2号 [['梅花', 7], ['黑桃', 7], ['红桃', 2]]
        3号 [['梅花', 14], ['红桃', 6], ['梅花', 6]]
        4号 [['方块', 13], ['红桃', 10], ['梅花', 2]]
        5号 [['黑桃', 13], ['梅花', 8], ['红桃', 8]]
        '''


# 判断牌的类型
def get_cards_type(player):
    tmp = player_puke_dic[player]
    if tmp[0][1] == tmp[1][1] and tmp[1][1] == tmp[2][1]:
        return 1      # 豹子
    elif tmp[0][0] == tmp[1][0] and tmp[1][0] == tmp[2][0]:
        if tmp[0][1] - 1 == tmp[1][1] and tmp[1][1] - 1 == tmp[2][1]:
            return 2  # 同花顺
        else:
            return 3  # 同花
    elif tmp[0][1] - 1 == tmp[1][1] and tmp[1][1] - 1 == tmp[2][1]:
        return 4      # 顺子
    elif tmp[0][1] == tmp[1][1] or tmp[1][1] == tmp[2][1]:
        return 5      # 对子
    else:
        return 6      # 单张


# 计算玩家牌的大小
def get_player_score():
    """
    计分方式：
    
    普通牌型，每张牌视为16进制的一个数，A对应14，2对应2，以此类推。牌值即为这幅此16进制牌的大小。比如最大的普通牌为AKJ，其16进制数值为AKJ=14x16x16+13x16+11=3803

    对子，先将对子放在牌前两位，则在最大普通牌大小的基础上，加上对子牌的本身大小。 对子的本身大小计算方法：比如最大的对子为AAK，则AAK=14x16+13=237，加上最大的普通牌值3803，即为4040

    顺子，取最小的那个数，加上最大的对子牌值，比如最大的顺子AKQ=12+4040=4052。最小的顺子A32，A取1，值4041

    同花，先按照普通牌型计算大小，再加上最大的顺子牌值。比如最大的同花AKJ=3803+4052=7855

    同花顺，取最小的那个数，加上最大的同花牌值，比如：AKQ=12+7855=7867,最小的同花顺A32，A取1，A32=1+7855=7856

    豹子，取第一个数，加上最大的同花顺牌值。比如AAA=14+7867=7881
    """
    for player, val in player_puke_dic.items():
        card_type = get_cards_type(player)
        # print(card_type, player, val)
        '''
        6 1号 [['梅花', 14], ['黑桃', 12], ['梅花', 3]]
        5 2号 [['梅花', 12], ['方块', 10], ['梅花', 10]]
        6 3号 [['红桃', 13], ['红桃', 7], ['梅花', 3]]
        6 4号 [['黑桃', 11], ['方块', 4], ['红桃', 2]]
        6 5号 [['红桃', 8], ['黑桃', 4], ['红桃', 3]]
        '''
        max_single = 3803
        max_double = 4040
        max_straight = 4052
        max_flush = 7855
        max_straight_flush = 7867
        # 单张
        if card_type == 6:
            score_dic[player] = val[0][1]*16*16+val[1][1]*16+val[2][1]
        # 对子
        elif card_type == 5:
            tmp_value = val[0][1]*16*16+val[1][1]*16+val[2][1]
            if val[0][1] == val[1][1]:
                score_dic[player] = max_single + tmp_value
            else:
                score_dic[player] = max_single + tmp_value
        # 顺子
        elif card_type == 4:
            score_dic[player] = max_double + min(val[0][1], val[1][1], val[2][1])
        # 同花
        elif card_type == 3:
            score_dic[player] = max_straight + val[0][1]*16*16+val[1][1]*16+val[2][1]
        # 同花顺
        elif card_type == 2:
            score_dic[player] = max_flush + min(val[0][1], val[1][1], val[2][1])
        # 豹子
        elif card_type == 1:
            score_dic[player] = max_straight_flush + val[0][1]


def find_winner():
    deal()
    sort_player_puke()
    get_player_score()
    tmp = []
    for player, score in score_dic.items():
        tmp.append(score)
    tmp = max(tmp)
    win = ""
    print("玩家有：")
    for player, score in score_dic.items():
        print(f"{player}  ", end='')
        print("权重：", score)
        if score == tmp:
            win = player
    print(f"\n赢家是： {win}")


if __name__ == '__main__':
    find_winner()
