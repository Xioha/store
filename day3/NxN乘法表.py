'''
使用while循环实现NxN乘法表的打印;
'''
def f(n):
    a = 1
    while a <= n:
        b = 1
        while b <= a:
            print("%d*%d=%d" % (b, a, a*b), end="\t")
            b += 1
        print("")
        a += 1
n = int(input("请输入”n“的值："))
f(n)  #阶层表显示