from random import randint

money = 1000
while money > 0:
    print('你的总资产为：', money)
    needs_go_on = False
    while True:
        Ran = randint(1, 12)
        num = Ran
        debt = int(input('请下注：'))
        if 0 < debt <= money:
            break
        if num == (7,11):
            print("玩家胜")


