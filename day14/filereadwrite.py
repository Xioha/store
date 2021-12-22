"""
    r:读取
    w：写入
    +:可读可写
    a:附加

    b:字节：mp3,mp4,图片
"""
# f1 = open(file="白冰.jpg",mode="rb")
# f2 = open(file="D:\\白冰.jpg",mode="wb")
#
# data = f1.read()
# f2.write(data)
# print(data)


# # 1、打开文件
# file = open("古诗.txt")
# # 2、读取文件内容
# text = file.read()
# print(text)
# # 3、关闭文件
# file.close()






import time
f1 = open(file="baidu_x_system.log",mode="r+",encoding="utf-8")
data = []
data1 = {}
for line in f1.readlines():
    line = line.strip("\n")
    line = line.split()
    data.append(line)
print(data)
while True:
    for i in range(len(data)):
        data1[data[i][0]] = 0
        for y in range(1,len(data)-1):
            if data[i][0] == data[y][0]:
                continue
            else:
                data1[data[i][0]] = 0
    for i in data1:
        for y in range(len(data)):
            if i == data[y][0]:
                data1[i] += 1
        print("用户ip为：",i,"访问了",data1[i],"次")
    time.sleep(5)   # 停留五秒种
