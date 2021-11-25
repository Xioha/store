'''
  从键盘依次输入10个数，最后打印10个数总和、最大的数、最小的数和平均数。

'''
print("=====================")
print("*   输入十个数字计算器  *")
print("=====================")
one = float(input("请输入数字："))
two = float(input("请输入数字："))
stree = float(input("请输入数字："))
four = float(input("请输入数字："))
five = float(input("请输入数字："))
six = float(input("请输入数字："))
seven = float(input("请输入数字："))
eight = float(input("请输入数字："))
nine = float(input("请输入数字："))
ten = float(input("请输入数字："))

list = [one, two, stree, four, five, six, seven, eight, nine, ten]

print("数字总和为：", sum(list))
print("最大数为：", max(list))
print("最小数为：", min(list))
print("平均数为：", sum(list)/len(list))