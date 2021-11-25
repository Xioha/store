A = 56
B = 78
def swap02(A, B):
    print("A=%d，B=%d" % (A, B))
    A = A+B
    B = A-B
    A = A-B
    print("实现效果：")
    print("A=%d，B=%d" % (A, B))
swap02(A, B)