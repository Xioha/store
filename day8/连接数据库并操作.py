"""
    1.联网安装pymysql
        pip install pymysql
    2.导入pymysql
    3.连接数据库
    4.创建控制台
    5.准备一条语句
        增，删，改：
            提交
        查询：
            提取数据
            fetchone()
            fetchall()
            fetchmany(size)

    6.提交数据到数据库
    7.关闭各项资源

"""
import pymysql

con = pymysql.connect(host="localhost",user="root",password="",database="company")

# 创建控制台
cursor = con.cursor()


# 执行语句

# SELECT 选择、 FROM 在、 WHERE 条件
# 查询所有的经理
cursor.execute("SELECT ename FROM t_employees WHERE job='经理';")
print("1、经理岗位员工：",cursor.fetchall())
# 查询在1995年到2000年入职的员工
cursor.execute("SELECT ename FROM t_employees WHERE hiredate>'1995-01-01' and hiredate<'2000-01-01';")
print("2、入职日期在1995-2000年间：",cursor.fetchall())
cursor.execute("SELECT ename FROM t_employees WHERE hiredate>'1900-01-01' and hiredate<'2000-01-01';")
print("\t入职日期在1900-2000年间随机一名员工：",cursor.fetchone())
cursor.execute("SELECT ename FROM t_employees WHERE hiredate>'1900-01-01' and hiredate<'2000-01-01';")
print("\t入职日期在1900-2000年间随机两名员工：",cursor.fetchmany(2))
# 找出奖金高于工资的员工
cursor.execute("SELECT * FROM t_employees WHERE comm > sal;")
print("3、奖金高于工资员工：",cursor.fetchall())
# 找出奖金高于工资60%的员工。
cursor.execute("SELECT * FROM t_employees WHERE (comm > sal*0.6);")
print("4、奖金高于工资60%的员工：",cursor.fetchall())
# 找出部门编号为10中所有经理，和部门编号为20中所有分析员的详细资料。
cursor.execute("SELECT * FROM t_employees WHERE deptno='10' AND job='经理' OR deptno=20 AND job = '分析员';")
print("5、编号条件查找的员工：",cursor.fetchall())
# 找出部门编号为10中所有经理，部门编号为20中所有分析员，还有即不是经理又不是武装上将但其工资大或等于3000的所有员工详细资料。
cursor.execute("SELECT * FROM t_employees WHERE	deptno='10' AND job='经理' OR deptno=20 AND"
               " job = '分析员' OR job != '经理' AND job!= '武装上将' AND sal >= 3000;")
print("6、按工资查指定职位员工：",cursor.fetchall())
# 无奖金或奖金低于1000的员工。
cursor.execute("SELECT ename FROM t_employees WHERE comm = NULL OR comm < 1000;")
print("7、奖金低于1000的员工：",cursor.fetchall())
# 查询名字由三个字组成的员工。
cursor.execute("SELECT ename FROM t_employees WHERE CHAR_LENGTH(ename) = 3;")
print("8、按名字字数查询：",cursor.fetchall())

#  关闭资源
cursor.close()
con.close()
# 获取数据
# data = cur.fetchall()
# print(data)
# for i in data:
#         print(i)
