from DBUtils import  update
from DBUtils import select


sql = "select * from user where money > %s"
param = []

data = select(sql,param,mode="many",size=3)

for i in data:
    print(i)






