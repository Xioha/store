
#阶乘计算： n！=1*2*3*4......*n

x = eval(input("请输入整数："))
t = 1
for i in range(1, x+1):
    t = t*i
print(t)
def CallNum(num):
    i = 1
    result = 1
    while i <= num:
        result *= i
        i += 1

    return result
