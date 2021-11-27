'''
有下列列表，请编程实现列表的数据翻转（京东金融的测试开发笔试题）
List = [1,2,3,4,5,6,7,8,9]
实现效果：list = [9,8,7,6,5,4,3,2,1]

'''
#方法一    ”使用reversed函数，reversed的结果是一个反转的迭代器“
listnumber = [1, 2, 3, 4, 5, 6, 7, 8, 9]
newlist = list(reversed(listnumber))    #list(reversed( ))列表中数据实现反转
print(newlist)

#方法二    “使用sorted函数，sorted是排序函数”
listnumber = [1, 2, 3, 4, 5, 6, 7, 8, 9]
newlist = sorted(listnumber, reverse=True)
print(newlist)

#方法三   “使用切片技术”
listnumber = [1, 2, 3, 4, 5, 6, 7, 8, 9]
fz = listnumber[::-1]
print(fz)