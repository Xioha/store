'''
一只青蛙掉在井里了，井深20米，青蛙白天网上爬3米，晚上下滑2米，问第几天能出来？请编程求出。
'''
depth = 20  # 井深20米
up = 3  # 上爬3米
down = 2  # 下滑2米
day = 0  # 刚掉下去时
while 1:
    # 计算结果每天1米
    depth -= up
    if depth <= 0:
        break
    depth += down
    day += 1
print("答：青蛙第", day, "天能爬上来。")