import random
from faker import Faker

alex = Faker(locale="zh_CN")  # zh_TW
staff_list = []
for i in range(300):
    staff_list.append(alex.name())
print(staff_list)

level = [30, 6, 3]

for i in range(3):
    winner_list = random.sample(staff_list, level[i])
    for w in winner_list:
        staff_list.remove(w)
    print(f"抽中{3-i}等奖的人是", winner_list)
