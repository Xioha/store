"""
一个蛋挞店有三个厨师做蛋挞，做好后盛在一个篮子里，最多盛500个蛋挞；
满了停3秒钟，然后判断是否已满，没满厨师继续做；
有六个客户抢着买，每个客户都有30000元，每个蛋挞3元，3分钟入一次帐；
每3分钟给厨师结一次帐，按每个蛋挞1.5元的工资。
"""
from threading import Thread
import time
most = 0
money = 30000*6
class chef(Thread):
    name = ""
    dan = 0

    def run(self) -> None:
        global most
        while True:

            if most < 500:
                self.dan = self.dan + 1
                most = most + 1
                print("美味的蛋挞出锅，",self.name,"做了一个蛋挞放入了篮子里，已经做了",most,"个蛋挞！")
                most == 500 and time.sleep(3)
                print("篮子盛满了，休息一下！")
                #
            else:
                print(self.name, "总共做了",self.dan,"个蛋挞！ 拿到",self.dan*1.5,"元工资。")

class client(Thread):
    name1 = ""
    mai = 0
    def run(self) -> None:
        global most, money
        while True:
            if most > 0 and money > 3:
                self.mai = self.mai + 1
                most = most - 1
                money = money - 3
                print("真香，",self.name1,"买了一个蛋挞并吃了起来！ 已经买了",most,"个蛋挞！")
            if money < 3:
                print(self.name1, "钱已经花光了，总共买了", self.mai, "个蛋挞！")
                break
            else:
                break

p1 = chef()
p2 = chef()
p3 = chef()
p1.name = "康师傅"
p2.name = "王师傅"
p3.name = "张师傅"
p1.start()
p2.start()
p3.start()

k1 = client()
k2 = client()
k3 = client()
k4 = client()
k5 = client()
k6 = client()
k1.name1 = "强子"
k2.name1 = "磊子"
k3.name1 = "大志"
k4.name1 = "凯儿"
k5.name1 = "胖子"
k6.name1 = "老李"
k1.start()
k2.start()
k3.start()
k4.start()
k5.start()
k6.start()
