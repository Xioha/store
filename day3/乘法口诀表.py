'''
编程实现99乘法表的倒叙打印

'''
print("倒序")
for a in range(9, 0, -1):
    for b in range(1, a+1, 1):
        print(str(b)+"x"+str(a)+"="+str(a*b), end="\t")
    print("")
print("顺序")
a = 1
while a <= 9:
    b = 1
    while b <= a:
        print(str(b)+"x"+str(a)+"="+str(a*b), end="\t")
        b += 1
    print("")
    a += 1