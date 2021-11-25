'''
  实现输入10个数字，并打印10个数的求和结果

'''
print("=====================")
print("* 输入十个数字求和计算器 *")
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