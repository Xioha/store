"""
题目一：
考查继承：继承的传递性
按要求定义类
要求：
1、定义厨师类，有姓名和年龄的属性，且属性私有化，提供相应的getXxx与setXxx方法，提供无返回值的无参数的蒸饭方法；
2、定义厨师的子类，该类中要求只能写一个无返回值的无参数的炒菜的方法，其他的方法不能写；
3、定义厨师的子类的子类，重写所有父类的方法，每个方法的内容只需打印一句话描述方法的功能即可；(蒸饭，炒菜)
4、定义测试类，创建厨师的子类的子类（厨师的孙子类）对象，使用该对象，对厨师类中的姓名和年龄属性赋值，并获取赋值后的属性值打印到控制台上；
5、使用厨师的孙子类对象调用该对象除了getXxx与setXxx以外的其他方法；

"""
class Chek:
    __name = ""
    __age = 0


    def Steam(self):
        pass

    def __set_name(self,name):
        self.__name = name
    def __get_name(self):
        return self.__name

    def __set_age(self, age):
        self.__age = age
    def __get_age(self):
        return self.__age


class Cheks(Chek):
    def fried(self):
        pass

class Chekss(Cheks):
    def Steam(self):
        print()
        print("正在蒸米饭")

    def fried(self):
        print()
        print("正在炒番茄鸡蛋")

    def set_age(self, param):
        pass

    def set_name(self, param):
        pass

    def get_name(self):
        pass

    def get_age(self):
        pass


if __name__ == '__main__':
    t = Chekss()
    t.set_age(20)
    t.set_name('张三')

    print('厨师叫%s，已经%s岁大了' % (t.get_name(), t.get_age()))

    t.Steam()
    t.fried()
