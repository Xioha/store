'''
外卖小哥
1、准备一个字典
2、字典内填入数据比如：#可以有不同的商铺和不同的地址2-3个就可以主要练习字典的定位和取值
dict_shop={"昌平":{"麻辣烫店":"麻辣烫","跑腿费":2,"客户地址":"101室"}}
dict_client={"昌平":{"翻斗花园":"101室"}}
3、商铺是随机产生的，地址也是随机产生的
4、适当的增加提示信息
5、一层一层去判断，如果shop的客户地址等于client的地址，就把外卖添加进去，增加跑腿费
6、最后定义函数，调用函数就可以了

'''
money = 0
dict_shop = {"昌平": {"麻辣烫店": "麻辣烫", "跑腿费": 2, "客户地址": "101室"}}
dict_client = {"昌平": {"翻斗花园": "101室"}}
boy = input("请输入您的地址")
import random
while True:
    d = input("请输入您要去的地址")
    if d in dict_shop:
        d2 = input("请输入您的商铺")
        if d2 in dict_shop[d]:
            print("恭喜您拿到饭了，开始送货")
            if dict_shop[d]["客户地址"] == dict_client["昌平"]["翻斗花园"]:
                dict_client["昌平"]["外卖"] = "麻辣烫"
                money = money+dict_shop[d]["跑腿费"]
                print("麻烦您支付服务费", money, "元")
                break
