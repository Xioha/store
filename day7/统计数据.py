"""
1.	统计和分析以下问题数据：
a)	统计所有表格中有多少人
b)	统计办电信，移动，联通的用户数量（14,17开头为电信）（13开头为移动）（15开头为联通）
c)	总公司男女人数
d)	年龄超过45岁的老员工人数
e)	薪资高于8000元的高薪人员数量和薪资低于3000的底薪人员数量
f)	统计去传媒公司的工作的人员数量
g)	统计一下可能在疫情高危地区的人数（高危地区：黑龙江，北京，福建，四川）

表格读取
"""
import xlrd  # 0.9.3
import xlwt
import numpy as np

baidu = xlrd.open_workbook(filename=r"百度合作单位-人员管理-二期.xls", encoding_override=True)
# wb.sheet_by_name()#名称
st = baidu.sheet_by_index(0)  # 位置
row = st.nrows  # 获取行数
col = st.ncols  # 获取列数

# 计算电信用户
dx = st.col_values(5,1)  # _values()获取一个范围
fw = [telecom for telecom in dx if telecom.startswith('14' or '17')]  # 获取指定项所在位置、.startswith为代表：以'14'或'17'开头的
telecom = len(fw)  # len获取值的长度或是个数
# 计算移动用户
yd = st.col_values(5,1)
fw1 = [link for link in yd if link.startswith('13')]
link = len(fw1)
# 计算联通用户
lt = st.col_values(5,1)
fw2 = [move for move in lt if move.startswith('15')]
move = len(fw2)
# 计算男女人数
man = st.col_values(8,1).count('男')  # .count获取项'男'在指定位置出现的次数
woman = st.col_values(8,1).count('女')
# 计算老员工
lr = st.col_values(7,1)
fw3 = [aging for aging in lr if aging > 45]  # 尾部直接可以取数值的范围
aging = len(fw3)
# 计算高薪人数
gx = st.col_values(11,1)
fw4 = [goodmoney for goodmoney in gx if goodmoney >= 8000]
goodmoney = len(fw4)
# 计算低薪人数
dx = st.col_values(11,1)
fw5 = [badmoney for badmoney in dx if badmoney <= 3000]
badmoney = len(fw5)
# 计算去传媒公司员工
cm = st.col_values(13,1)
fw6 = [position for position in cm if position.endswith('传媒有限公司')]  # .endswith代表字段中包含有'传媒有限公司'
position = len(fw6)
# 计算黑龙江人数
hlj = st.col_values(9,1)
fw7 = [heilongjiang for heilongjiang in hlj if heilongjiang.startswith('黑龙江')]
heilongjiang = len(fw7)
# 计算北京人数
bj = st.col_values(9,1)
fw8 = [beijing for beijing in bj if beijing.startswith('北京')]
beijing = len(fw8)
# 计算福建人数
fj = st.col_values(9,1)
fw9 = [fujian for fujian in fj if fujian.startswith('福建')]
fujian = len(fw9)
# 计算四川人数
sc = st.col_values(9,1)
fw10 = [sichuan for sichuan in sc if sichuan.startswith('四川')]
sichuan = len(fw10)

# 打印各项数据
print("1、表格中人数共：",row,"人")
print("2、表格中电信用户共：",telecom,"人"),print("\t表格中移动用户共：",link,"人"),print("\t表格中联通用户共：",move,"人")
print("3、表格中男性共：",man,"人"),print("\t表格中女性共：",woman,"人")
print("4、表格中老员工：",aging,"人")
print("5、表格中高薪员工：",goodmoney,"人"),print("\t表格中低薪员工：",badmoney,"人")
print("6、表格中传媒公司员工：",position,"人")
print("7、表格中黑龙江人数：",heilongjiang,"人"),print("\t表格中北京人数：",beijing,"人"),print("\t表格中福建人数：",fujian,"人"),
print("\t表格中四川人数：",sichuan,"人")
