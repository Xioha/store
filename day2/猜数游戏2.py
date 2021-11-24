'''
需求：
1、猜的数字是系统产生的，不是自己定义的
2、键盘输入的   操作完填入：input（“提示”）
3、判断			操作完填入：if判断条件 elif 判断条件。。。。。。Else
4、循环			操作完填入：while 条件循环
任务：如果键盘输入大于随机数弹出友好提示信息“猜大了”，猜小了
起始金额  5000 才对一次给300 猜错扣除100 猜错15次结束
金额为0也结束
'''
import random
#   随机生成数字  （开始int，结束int）  []

money = 5000
i = 0
while True:
    Ran = random.randint(1, 20)
    num = input("请输入一个数字:\n")
    num = int(num)
    #  键盘输入  随机数
    if num == Ran:
        print("猜对了,奖励您三百哦，当前资产")
        money = money+300
        print(money)
    elif num > Ran:
        print("猜大了，不好意思扣您一百，当前资产")
        money = money-100
        i += 1
        print(money)
    else:
        print("猜小了，不好意思扣您一百，当前资产")
        money = money-100
        i += 1
        print(money)
    if money == 0:
        print("对不起，你已经破产了：")
        print(money)
        break
    if i == 15:
        print("抱歉，你猜错次数太多了")
        break  #退出