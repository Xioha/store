"""
请编程
i.	人：年龄，性别，姓名。
ii.	现在有个工种，工人：年龄，性别，姓名 。行为：干活。请用继承的角度来实现该类。
iii.现在有学生这个工种，学生：年龄，性别，姓名，学号。行为：学习，唱歌。请结合上面的几个题目用继承的角度来实现。
"""

import time
class person:
    name = ""
    sex = ""
    age = 0



class worker(person):
    def works(self,working):
        for i in range(4):
            print(".",end="")
            time.sleep(1)
        print(self.name,"性别",self.sex,"年龄",self.age,"岁,职业：工人，正在",working,"!!!")

class student(person):
    def studys(self,study,sing):
        for i in range(4):
            print(".",end="")
            time.sleep(1)
        print(self.name,"性别",self.sex,"年龄",self.age,"岁,是一名大学生，正在边",study,"边",sing,"!!!")


work = worker()
work.name = "杰森·斯坦森"
work.sex = "男"
work.age = 27

work.works("进行赛车比赛")

study = student()
study.name = "小明同学"
study.sex = "男"
study.age = 17
study.studys("学习弹吉他","唱情歌")
