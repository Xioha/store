'''
输入三个数字进行组合，判断可否组成三角形，进而判断三角形类型；
如下：
'''
print(" 三角形是如何组成的 ")
print("设定边长分别为a、b、c")
a = float(input("请输入a的长度："))
b = float(input("请输入b的长度："))
c = float(input("请输入c的长度："))
if a<b+c and b<a+c and c<a+b and a>c-b and a>b-c and b>a-c and b>c-a and c>a-b and c>b-a:
    print("a=%s,b=%s,c=%s 可以组成三角形" % (a, b, c))
    if a == b or b == c or a == c:
        print("a=%s,b=%s,c=%s 可以组成等腰三角形" % (a, b, c))
    if a == b == c:
        print("a=%s,b=%s,c=%s 可以组成等边三角形" % (a, b, c))
    elif a**2+b**2==c**2 or b**2+c**2==a**2 or c**2+a**2==b**2:
        print("a=%s,b=%s,c=%s 可以组成直角三角形" % (a, b, c))
    else:
        print("a=%s,b=%s,c=%s 组成普通三角形" % (a, b, c))
else:
    print("a=%s,b=%s,c=%s 不能组成三角形" % (a, b, c))