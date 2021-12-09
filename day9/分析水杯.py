"""
分析一个水杯的属性和功能，使用类描述并创建对象
高度，容积，颜色，材质
能存放液体

"""
# import time
class cup:
    __height = 0
    __cubage = 0.0
    __colour = ""
    __texture = ""
    __liquid = ""



    def setheight(self,height):
        if height > 80 or height < 0:
            print("高度非法！别瞎弄！")
        else:
            self.__height = height

    def getheight(self):
        return self.__height

    def setcubage(self,cubage):
        if cubage > 100 or cubage < 0:
            print("容积非法！")
        else:
            self.__cubage = cubage

    def getcubage(self):
        return self.__cubage



    def colour(self):
        print(self.colour)

    def texture(self):
        print(self.texture)


    def cup(self):
        print("水杯高",self.__height,"厘米，容积为",self.__cubage,"升,颜色是：",self.colour,"，材质为：",self.texture)




p = cup()

# p.height = "20"
p.setheight(20)
# p.cubage = 0.5
p.setcubage(0.5)
p.colour = "透明白色"
p.texture = "玻璃"

p.cup()
