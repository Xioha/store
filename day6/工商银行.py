"""
运用编程写出”中国工商银行“操作系统

"""
# from random import randint
import random

print("===============")
print("|  中国工商银行 |")
print("===============")
print("|1、开户       |")
print("|2、存钱       |")
print("|3、取钱       |")
print("|4、转账       |")
print("|5、查询       |")
print("===============")
# 定义一个空字典,当作数据库
bank = {}
# bank={'Frank': {'account': 29073386, 'password': '123456', 'country': '中国', 'province': '山东', 'street': '1大街',
# 'door': '001', 'bank_name': '中国工商银行', 'money': 0}
bank_name = "中国工商银行"

# 定义方法————用来添加用户的
def useradd():
    account = random.randint(10000000, 99999999)
    username = input("请输入您的用户名")
    password = input("请输入您的密码")  # 如果定义为str   ”“
    country = input("\t\t请输入您的国家")  # \t表示一个tab
    province = input("\t\t请输入您的省份")
    street = input("\t\t请输入你的街道")
    door = input("\t\t请输入您的门牌号")
    gift = bankadd(account, username, password, country, province, street, door)  # 位置对应
    if gift == "1":
        print("开户成功,以下是您的详细信息")
        # 模板
        info = '''
                --------工商银行-------
                    1、账号：%s
                    2、用户名：%s
                    3、密码：******
                    4、国家：%s
                    5、省份：%s
                    6、街道：%s
                    7、门牌：%s
                    8、余额：%s
                    9、开户行：%s
        '''
        print(info % (account, username, country, province, street, door, bank[username]["money"], bank_name))
    elif gift == "2":
        print("请使用其他用户")
    elif gift == "3":
        print("数据库已满")

# 往字典里面存数据
def bankadd(account, username, password, country, province, street, door):
    if username in bank:  # 姓名在不在bank的键里
        return "2"
    elif len(bank) >= 100:
        return "3"
    bank[username] = {
        "account": account,  # 从useradd的account获取的随机数
        "password": password,
        "country": country,
        "province": province,
        "street": street,
        "door": door,
        "bank_name": bank_name,
        "money": 0
    }
    return "1"
# 定义存钱
def saveadd(username):
    if username in bank:
        print("您账户余额为：%s" % bank[username]["money"])
        money = int(input("请输入存钱金额：")) + bank[username]["money"]
        bank[username]["money"] = money
        return True
    else:
        return False
# 定义取钱
def fetchadd(username, password):
    if username in bank and password == bank[username]["password"]:
        print("您账户余额为：%s" % bank[username]["money"])
        money = bank[username]["money"] - int(input("请输入取钱金额："))
        if money >= 0:
            bank[username]["money"] = money
            return "1"
        elif money < 0:
            return "2"
    elif username not in bank:
        return "3"
    elif username in bank:
        if password != bank[username]["password"]:
            return "4"
# 定义转账
def transferadd(zr_name, zc_name, password):
    if zr_name in bank and zc_name in bank:
        if password == bank[zc_name]["password"]:
            zrmoney = int(input("请输入转入金额："))
            money = bank[zc_name]["money"] - zrmoney
            if money >= 0:
                bank[zc_name]["money"] = money
                return 1
            elif money < 0:
                return 2
        elif password != bank[zc_name]["password"]:
            return 3
    elif zr_name not in bank:
        return 4
    elif zc_name not in bank:
        return 5
# 定义查询
def inquireadd(username, password):
    if username in bank and password == bank[username]["password"]:
        return 1
    elif username not in bank:
        return 2
    elif password != bank[username]["password"]:
        return 3


# 执行存钱
def cqadd():
    username = input("请输入用户名：")
    cq = saveadd(username)
    if cq:
        info = '''
            ======交易信息=====
            账号：%s
            用户名：%s
            余额：%s
            开户行：%s
        '''
        # 可以传入已定义的元素
        print(info % (bank[username]["account"], username, bank[username]["money"], bank_name))
    elif not cq:
        print("用户名不存在！")
# 执行取钱
def qqadd():
    username = input("请输入用户名：")
    password = input("请输入密码：")
    qq = fetchadd(username, password)
    if qq == "1":
        info = '''
            =====交易信息=====
            账号：%s
            用户名：%s
            余额：%s
            开户行：%s
        '''
        # 可以传入已定义的元素
        print(info % (bank[username]["account"], username, bank[username]["money"], bank_name))
    elif qq == "2":
        print("用户余额不足！")
    elif qq == "3":
        print("用户不存在！")
    elif qq == "4":
        print("输入密码错误！")
# 执行转账
def zzadd():
    zr_name = input("请输入转入用户名：")
    zc_name = input("请输入转出用户名：")
    password = input("请输入账户密码：")
    zz = transferadd(zr_name, zc_name, password)
    if zz == 1:
        info = '''
            =====交易信息=====
            转出用户名：%s
            转入用户名：%s
            余额：%s
            开户行：%s
        '''
        print(info % (zc_name, zr_name, bank[zc_name]["money"], bank_name))
    if zz == 2:
        print("账户余额不足！")
    elif zz == 3:
        print("账户密码错误！")
    elif zz == 4:
        print("转入用户名不存在！")
    elif zz == 5:
        print("转出用户名不存在！")
# 执行查询
def cxadd():
    username = input("请输入用户名：")
    passwrod = input("请输入密码：")
    cx = inquireadd(username, passwrod)
    if cx == 1:
        print("查询信息如下：")
        info = '''
            =====账户信息=====
            账号：%s
            用户名：%s
            余额：%s
            开户行：%s
            '''
        print(info % (bank[username]["account"], username, bank[username]["money"], bank_name))
    elif cx == 2:
        print("用户不存在！")
    elif cx == 3:
        print("输入密码错误！")


# 各种操作的循环命令
while True:
    box = input("请输入您要办理的业务")
    if box == "1":
        print("1、开户")
        useradd()
    elif box == "2":
        print("2、存钱")
        cqadd()
    elif box == "3":
        print("3、取钱")
        qqadd()
    elif box == "4":
        print("4、转账")
        zzadd()
    elif box == "5":
        print("5、查询")
        cxadd()
    elif box == "6":
        print("byb")
        break
