#实现登陆系统的三次密码输入错误锁定功能（用户名：root,密码：admin）
username='root'
password='admin'
list=[]
for i in range(0,3):
    inusername=input("用户名：")
    inpassword=input("密码：")
    if inusername==username and inpassword==password:
        print("正在登陆中...")
        break
    elif inusername!=username or inpassword!=password:
        print("输入的用户名或密码错误")
    if i>=2:
        list.append(inusername)
if inusername in list:
    print("该账号已锁定，请解锁后登陆")