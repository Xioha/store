'''
编程实现图形的打印；
'''
c = 1      #层数
while c <= 7:
    k = 6  #添加空白
    while k >= c:
        print(' ', end='')
        k -= 1
    x = 1  #图形符号
    while x <= c:
        print('*', end=' ')
        x += 1
    c += 1
    print()  # 空行