'''
  实现登陆系统的三次密码输入错误锁定功能（用户名：root,密码：admin）

'''
time = 1
username = "root"  # 登录用户名
user_password = "admin"   # 登录密码

name = input("请输入用户名：")

if name == username:
    while time <= 3:
        password = input("请输入密码：")
        if name == username and password == user_password:
            print("欢迎%s!"%name)
            break
        else:
            print("账号和密码不匹配！""\n""请重新输入密码：")
            time += 1
    else:
        print("对不起，账号已被锁定！")
else:
    print("用户不存在！")