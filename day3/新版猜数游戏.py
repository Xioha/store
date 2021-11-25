'''
猜字游戏：
需求：
1、猜的数字是系统产生的，不是自己定义的
2、键盘输入的   操作完填入：input（“提示”）
3、判断			操作完填入：if判断条件 elif 判断条件。。。。。。Else
4、循环			操作完填入：while 条件循环
#任务：开始金币有5个金币，每猜一次减一个为0就退出（or充钱）猜错3次也退出
'''
import random
#              20，10
randint = random.randint(10, 20)#随机生成数字的范围：int   []
print(randint)

gold = 5
i = 0
print("您拥有%d个金币"%gold)
while i <= 3:
    num = int(input("谜底提示：取值的范围为10-20之间：\n"))
    if num == randint:
        print("恭喜你猜对了，你还有%d次机会" % (gold-1))
        print("还有%d个金币了。" % (gold-1))
        gold = gold-1
    elif num > randint:
        print("猜大了，还有%d个金币，" % (gold-1))
        print("还有%d次机会了。" % (gold-3))
        gold = gold-1
        i += 1
    else:
        print("猜小了，还有%d个金币，" % (gold-1))
        print("还有%d次机会了。" % (gold-3))
        gold = gold-1
        i += 1
    if gold == 0:
        print("对不起，请先充值：")
        e = int(input())
        gold = gold+e
    if i == 3:
        print("抱歉，你猜错次数太多了！")
        break  #退出

