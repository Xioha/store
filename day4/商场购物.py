'''
    Frank的商城：
        1.准备商品
        2.空的购物车
        3.钱包初始化金钱
        4.最后打印购物小条
    1.业务：
        看到商品：
            商品存在
                看金钱够：
                    成功加入购物车。
                    余额减去对应价格。
                不够：
                    穷鬼，去买其他商品。
            商品不存在：
                输入错误。
            输入Q或q，退出并结算。打印小条。
    任务：尽量多的添加商品
    任务：10个辣条优惠券（0.3），20个威猛先生优惠券（0.9），免单一张优惠券，先整体打折8后在单独打折，
        在进入商城时，随机抽取优惠券，在最后结算使用改优惠券。
'''
#超市
shop=[
    # 0     1
    ["方便面",5],#0
    ["卫龙",5.5],#1
    ["百岁山",3],#2
    ["好丽友",6],
    ["鸡蛋挂面",10],
    ["中华香烟",70],#抽烟
    ["电磁炉",299],
    ["保温杯",129],
    ["沐浴露",58],
    ["清扬洗发水",60],
    ["蓝月亮",90],
    ["威猛先生",60],
    ["躺椅",100],
    ["拖把",30],
    ["洗衣机",999]

]
#购物车
mycar=[]
#初始化钱包
money=1000
#       枚举


while True:
    for i in enumerate(shop):#列举商品
        print(i)
    o=input("请选择商品")#str  转换成int类型
    # 一个元素在某一个容器里面：
    if o.isdigit():#.isdigit判读字符串内是不是由数字组成
        o=int(o)#把str转换成int
        if o <len(shop):#判断输入的范围
            if money>shop[o][1]:#钱够不够
                mycar.append(shop[o])#加入购物车
                print(mycar)
                money=money-shop[o][1]#减钱
                print("此商品已经加入购物车，您的余额为：",money)
            else:print("穷鬼，gun")
        else:print("请输入正确的商品编号")
    elif o =="q" or o=="Q":#输入内容退出并打印小条
        print("再见,以下是您购买的商品")
        for i in enumerate(mycar):
            print(i)
        break
    else:print("您输入的有误")

import random
prize = ["辣条3折券","辣条3折券","辣条3折券","辣条3折券","辣条3折券","辣条3折券","辣条3折券",
         "辣条3折券","辣条3折券","辣条3折券",
         "威猛先生9折券","威猛先生9折券","威猛先生9折券","威猛先生9折券","威猛先生9折券",
         "威猛先生9折券","威猛先生9折券","威猛先生9折券","威猛先生9折券","威猛先生9折券",
         "威猛先生9折券","威猛先生9折券","威猛先生9折券","威猛先生9折券","威猛先生9折券",
         "威猛先生9折券","威猛先生9折券","威猛先生9折券","威猛先生9折券","威猛先生9折券",
         "今日免一单",
         "全场商品8折券","全场商品8折券","全场商品8折券","全场商品8折券","全场商品8折券",
         "全场商品8折券","全场商品8折券","全场商品8折券",]
print("顾客您好，今日商场进行抽奖活动！")

result = random.choice(prize)
time = 0
while True:
    cj = int(input("输入任意“整数”抽奖："))
    print("恭喜您使用：",result)
    time += 1

    if result == "辣条3折券":
        for i in mycar:
            if i[0] == "卫龙":
                money = money + i[1] - i[1]*0.3
        print("使用奖券后，你余额还剩：", money, "元")
    if result == "威猛先生9折券":
        for i in mycar:
            if i[0] == "威猛先生":
                money = money + i[1] - i[1]*0.9
        print("使用奖券后，你余额还有剩：", money, "元")
    if result == "今日免一单":
        print("使用奖券后，你余额还剩：", money, "元")
    if result=="全场商品8折券":
        for i in mycar:
            # num1 = sum(i[1]) * 0.8
            # money = money + sum(i[1]) - num1
            money = money + i[1] - i[1]*0.8
            print("使用奖券后，你余额还剩：", money)
            break
    if time == 1:
        break