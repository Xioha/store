"""
有笔记本电脑（屏幕大小，价格，cpu型号，内存大小，待机时长），
行为（打字，打游戏，看视频）
"""

class computer:
    __size = 0
    __price = 0
    __cpu = ""
    __storage = 0
    __duration = 0
# 给配置项名称定义
    def setsize(self,size):
        if size > 22 or size < 0:
            print("尺寸非法！")
        else:
            self.__size = size

    def getsize(self):
        return self.__size

    def setprice(self,price):
        if price < 0:
            print("价格非法！")
        else:
            self.__price = price

    def getprice(self):
        return self.__price

    def cpu(self):
        print(self.cpu)

    def storage(self):
        print(self.storage)

    def setduration(self,duration):
        if duration > 12 or duration < 0:
            print("时长非法！")
        else:
            self.__duration = duration

    def getduration(self):
        return self.__duration

    def type(self,essay,hour):
        print("作者正在打字，写作",essay,"全集",self.cpu,"已经运行了",hour,"小时！")

    def play(self,game,hour):
        print("玩家正在打",game,self.cpu,"已经运行了",hour,"小时！")

    def video(self,look,hour):
        print("追剧狂徒正在看",look,self.cpu,"已经运行了",hour,"小时！")

    def computer(self):
        print("此电脑配置为： \n屏幕尺寸：",self.__size,"寸， 售价：",self.__price,"RMB， 处理器型号：",self.cpu,"， 内存：",
              self.__storage,"GB， 待机时长：",self.__duration,"小时")

p = computer()
# 对象属性
p.setsize(15)
p.setprice(2988)
p.cpu = "11th i5intel"
p.storage = 500
p.setduration(5)
# 对象行为
p.type("《平凡的世界》",3)
p.play("王者荣耀",2)
p.video("水浒传",2)
# 对象显示
p.computer()
