# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 14:51:31 2021

@author: Domenic
"""

fr = open("data/account.db", mode="r", encoding="UTF-8")

accounts = {
    # 存储的信息例子
    # "alex":["abc123!","1"],
}

# 逐行读入，产生 字典account 和 数组line
for line in fr:
    line = line.strip().split(',')
    print(line)
    accounts[line[0]] = line[1:]  
    
# 3. 搞个loop , 要求用户输入账号信息， 判断
flag = 0
while flag == 0:
    if_new_account = 0
    username = input("Username: ")
    if username.strip() not in accounts:
        print("您未注册...", end='')
        if input("现在是否注册？ (Y/N) ").strip() == 'Y':  # 注册
            tmp = []
            new_username = input("Username: ")
            tmp.append(new_username)
            tmp.append(input("Password: "))
            tmp.append("0")
            accounts[tmp[0]] = tmp[1:]
            print(f"恭喜 {new_username} 注册成功！")
            if_new_account = 1
        else:                                            # 不注册
            if input("已有账号，是否登录？ (Y登录/N退出) ") == 'Y':
                continue
            else:
                break
    elif accounts[username][1] == "1":
        print("该账户已被锁定，请联系管理员")
        break
    
    cnt = 1
    while cnt <= 3:
        if cnt == 1:  # 只有第一次显示
            if if_new_account == 1:
                print("Username: ")
            psw = input("Password: ")
        
        if accounts[username][0] == psw:
            print("登录成功!")
            flag = 1
            break
        else:
            cnt += 1
            psw = input(f"密码错误！ 您还有 {3-cnt+1} 次机会，请重新输入： ")
    
    if cnt == 3:
        accounts[username][1] = "1"
        print(f"您输错了 {cnt} 次密码，账户 {username} 已被锁定！")
        
    fw = open("data/account.db", mode="w", encoding="UTF-8")
    # print(accounts.items())
    '''
    items()输出
    dict_items([('alex', ['abc123!', '1']), ('jack', ['ssss3', '1']), ('rain', ['ab333s', '0'])])
    '''
    for username, val in accounts.items():
        print()
        val.insert(0, username)  # 头插insert
        print(val)
        line = ",".join(val) + "\n"  # 把列表再转成字符
        fw.write(line)
    fw.close()
    
fr.close()

print("\n再见!")
