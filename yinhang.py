# 确定用户库
bank = {
    "12312312": {"username": "zp", "password": "123456", "country": "中国", "province": "北京", "street": "温泉", "door": "1",
               "money": 30000, "bank_name": "中国工商银行昌平区回龙观支行"},
    '35163969': {'username': '1', 'password': '1', 'country': '1', 'province': '1', 'street': '1', 'door': '1',
                 'money': 500, 'bank_name': '中国工商银行昌平区回龙观支行'},
    '35163968': {'username': '1', 'password': '1', 'country': '1', 'province': '1', 'street': '1', 'door': '1',
                 'money': 100, 'bank_name': '中国工商银行昌平区回龙观支行'},
    }
# 确定银行的开户名称
bank_name = "中国工商银行昌平区回龙观支行"

info = '''
    *********************************
    *    中国工商银行账户管理系统     *
    *********************************
    *   1.开户                      *
    *   2.存款                      *
    *   3.取款                      *
    *   4.转账                      *
    *   5.查询账户                  *
    *   6.Bye！                     *
    ********************************
'''
import random
import sys

# 银行的开户逻辑
def bank_addUser(account, username, password, country, province, street, door, money):
    # 判断用户库是否已满
    if len(bank) >= 100:
        return 3

    # 判断是否存在
    # 获取所有键，然后在判断是否有
    keys = bank.keys()
    if account in keys:
        return 2
    # 正常开户
    bank[account] = {
        "username": username,
        "password": password,
        "country": country,
        "province": province,
        "street": street,
        "door": door,
        "money": money,
        "bank_name": bank_name
    }
    return 1


# 开户逻辑
def addUser():
    # 生成账号：  8位随机
    string = ""  # 随机数缓冲
    for i in range(8):  # 循环8次取字符

        string = string + "1234567890"[random.randint(0, 9)]  # 拼接

    account = string
    print("账号为：", account)
    username = input("请输入姓名：")
    password = input("请输入密码：")
    print("接下来输入地址信息：")
    country = input("\t输入国家：")
    province = input("\t输入省份：")
    street = input("\t输入街道：")
    door = input("\t输入门牌号：")
    money = int(input("请初始化您的余额："))

    # 调用银行的开户方法
    s = bank_addUser(account, username, password, country, province, street, door, money)

    if s == 1:
        print("开户成功！")
        print("以下是您的开户个人信息：")
        print("***********************")
        print("账号：", account)
        print("用户名：", username)
        print("密码：******")
        print("国家：", country)
        print("省份：", province)
        print("街道：", street)
        print("门牌号：", door)
        print("账户余额：", money)
        print("******************开户行地址：", bank_name)

    elif s == 2:
        print("该用户已存在！")
    elif s == 3:
        print("对不起，该银行已满！请携带证件到其他银行办理！")


def cunqian():
    account = input("请输入账号：")
    passwdd = input("请输入密码:")
    money = bank[account]["money"]
    passwd = bank[account]["password"]
    keys = bank.keys()
    if account in keys:
        if passwdd == passwd:
            cunqianshu = int(input("请输入您存钱的数量:"))
            money = cunqianshu + money
            print("您当前余额为：", money)
            return
        else:
            print("账号或密码错误!")


def getmoney():
    while 1:
        i = 0
        getnum = 0
        if chose == "3":
            account = input("请输入您的账户：")
            if account == "q":
                break
            elif account in bank.keys():
                while i < 3:
                    password = input("请输入您的密码：")
                    if account == "q":
                        break
                    elif password == bank[account]["password"]:
                        print("欢迎回来", account)
                        lost = bank[account]["money"]
                        print("您当前的账户余额为：", lost)
                        getnum = int(input("请输入您的取款金额："))
                        if getnum > lost:
                            print("您的余额不足，当前余额为：", lost)
                            return 3
                        lost = lost - getnum
                        print("您当前的账户余额为：", lost)
                        break
                    else:
                        print("密码不正确请重试")
                        i += 1
                        if i == 3:
                            return 2
            else:
                print("账户不正确，请重试")
                return 1


def sb():
    if chose == "4":
        a = input("请输入户名；")
        if a in bank.keys():
            print("对")
            b = input("请输入密码：")
            if b == bank[a]['password']:
                print("对")
                c = input("请输入转入用户：")
                if c in bank.keys():
                    print("对")
                    d = input("请选择转入金额:")
                    d = int(d)
                    if d <= bank[a]['money']:
                        bank[a]['money'] = bank[a]['money'] - d
                        bank[c]['money'] = bank[c]['money'] + d
                        print("转账成功", "当前余额", bank[a]['money'])
                        return 0
                    else:
                        print("转不了")
                        return 3
                else:
                    print("不存在")
                    return 1
            else:
                print("不正确")
                return 2
        else:
            print("不存在")
            return 1
    else:
        print("gun")


def inquire():
    if chose == "5":
        account = input("请输入账号：")
        if account in bank.keys():
            pwd = input("请输入该账号的密码")
            if pwd == bank[account]["password"]:
                print("当前账号:", account, "\n",
                      "密码为：", bank[account]["password"], "\n",
                      "余额为:", bank[account]["money"], "元", "\n",
                      "用户居住地址为：", bank[account]["country"], "-", bank[account]["province"], "-",
                      bank[account]["street"],
                      "-", bank[account]["door"], "\n",
                      "当前开户行为：", bank_name)
            else:
                print("密码输入错误")
        else:
            print("信息不存在")
    else:
        print("信息不存在")







while True:  # 一直循环的进入选项
    print(info)
    chose = input("请输入您的选项：")
    if chose == "1":  # 判断是否是1
        addUser()
    elif chose == "2":  # 判断是否是22
        cunqian()
    elif chose == "3":  # 判断是否是3
        getmoney()
    elif chose == "4":  # 判断输入的是否是4
        sb()
    elif chose == "5":  # 判断输入的是否是5
        inquire()
    elif chose == "6":  # 判断输入的是否是6，若是6则需要退出 break
        print("拜拜了您嘞！")
        sys.exit()
    else:
        print("输入非法！重新输入！")
