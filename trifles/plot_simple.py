# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 15:45:49 2021

@author: Domenic
"""
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

R = 80000

C = 25 * pow(10, -9)

Vs = 120

t = np.linspace(0, 0.015, 400)

Vc = Vs * (1 - np.power(np.e, -t/(R*C)))

plt.plot(t, Vc, )
matplotlib.rcParams['font.family'] = 'Arial'
matplotlib.rcParams['font.size'] = 14
plt.title('Capacitor voltage as a function of time')
plt.xlabel('Vc (V)')

'''
# 改变字体和大小
matplotlib.rcParams['font.family'] = 'simHei'
matplotlib.rcParams['font.size'] = 12
# 只希望在某地方绘制中文字符，不改变别的地方的字体
plt.xlabel('横轴：时间', fontproperties = 'simHei', fontsize = 12)
'''

plt.ylabel('t (s)')

plt.show()
