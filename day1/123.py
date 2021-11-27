import random

first = ["王","李","昂","在","看","了"]
name = random.choice(first)
while True:
    num = int(input("输入任意整数抽奖：\n"))
    print(name)