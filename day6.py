import random
print("***************************")
print("*    中国工商银行          *")
print("*     账户管理系统         *")
print("***************************")
print(" ")
print("*1、开户                   *")
print("*2、存钱                   *")
print("*3、取钱                   *")
print("*4、转账                   *")
print("*5、查询                   *")
print("*6、欢迎下次光临            *")
print("****************************")
#初始化银行
bank={}
#'Frank': {'account': 24275182, 'password': '123456', 'country': '中国', 'province': '山东', 'steert': '曹县', 'door': '001', 'money': 0, 'bank_name': '保熟银行'}
#定义一个开户银行
bank_name="保熟银行"

#定义添加到银行 定义函数元素对应元素  不是名称对名称
def bankadd(account,name,password,country,province,steert,door):
    if len(bank)>=100:
        return 3
    elif name in bank:
        return 2
    else:
        bank[name]={
            "account":account,
            "password":password,
            "country":country,
            "province":province,
            "steert":steert,
            "door":door,
            "money":0,
            "bank_name":bank_name
        }
        return 1

def cqadd(name):
   if name in bank:
       print("用户金额：%d"%bank[name]['money'])
       money=int(input("请输入您要存入的金额："))+bank[name]['money']
       bank[name]['money']=money
       return True
   else:
       return False

def qxadd(name,password):
    if name in bank and password==bank[name]['password']:
        print("用户金额：%d"%bank[name]['money'])
        money= bank[name]['money']-int(input("请输入您要取出的金额："))
        if money<0:
            return 3
        elif money>=0:
            bank[name]['money'] = money
            return 0
    elif name not in bank:
        return 1
    elif name in bank:
        if password != bank[name]['password']:
            return  2

def zzadd(zhuanchuname,zhuanruname,password):
    if zhuanchuname in bank and zhuanruname in bank:
        if password==bank[zhuanchuname]['password']:
            zhuanrumoney=int(input("请输入您要转出的金额："))
            money = bank[zhuanchuname]['money'] - zhuanrumoney
            if money < 0:
                return 3
            elif money>=0:
                bank[zhuanchuname]['money'] = money
                bank[zhuanruname]['money']=zhuanrumoney
                return 0

    if zhuanchuname not in bank or zhuanruname not in bank:
        return 1
    elif password !=bank[zhuanchuname]['password']:
        return 2

def cxadd(name,password):
    if name in bank and password==bank[name]['password']:
        return 0
    elif name not in bank:
        return 1
    elif password != bank[name]['password']:
            return 2







#定义用户入参
def useradd():
    account=random.randint(10000000,99999999)
    name=input("请输入您的名称")
    password=int(input("请输入您的密码"))
    print("请输入你的详细信息")
    country=input("\t\t请输入您的国籍")#\t ==tab
    province=input("\t\t请输入您的省份")
    steert=input("\t\t请输入您的街道")
    door=input("\t\t请输入您的门牌号")
    num=bankadd(account,name,password,country,province,steert,door)



    if num ==3:
        print("本银行已满请到其他银行开户")
    elif num== 2:
        print("用户已存在")
    elif num==1:
        print("恭喜你开户成功，一下是您的相信信息")
        info = '''
                   ------------个人信息------------
                   用户名:%s
                   账号：%s
                   密码：*****
                   国籍：%s
                   省份：%s
                   街道：%s
                   门牌号：%s
                   余额：%s
                   开户行名称：%s
               '''
        # 每个元素都可传入%
        print(info % (name, account, country, province, steert, door, bank[name]["money"], bank_name))


def cunqianadd():
    name=input("请输入您的姓名：")

    num1=cqadd(name)


    if num1==False:
        print("银行没有该用户信息")
    elif num1==True:
        info = '''
                           ------------个人信息------------
                           用户名:%s               
                           密码：*****
                           余额：%s
                           开户行名称：%s
                       '''
        # 每个元素都可传入%
        print(info % (name,bank[name]["money"], bank_name))

def quxianadd():
    name = input("请输入您的姓名：")
    password = int(input("请输入您的用户密码："))
    num2 = qxadd(name,password)

    if num2==1:
        print("账户信息不存在")
    elif num2==2:
        print("密码输入错误")
    elif num2==3:
        print("您的余额不足")
    elif num2==0:
        info = '''
                                   ------------个人信息------------
                                   用户名:%s               
                                   密码：*****
                                   余额：%s
                                   开户行名称：%s
                               '''
        # 每个元素都可传入%
        print(info % (name, bank[name]["money"], bank_name))

def zhuanzhangadd():
    zhuanchuname=input("请输入您转出账户的姓名：")
    zhuanruname=input("请输入您转入账户的姓名：")
    password = int(input("请输入您的用户密码："))
    num3=zzadd(zhuanchuname,zhuanruname,password)

    if num3==1:
        print("转出或转入的账号不存在")
    elif num3==2:
        print("转出账户的密码输入错误")
    elif num3==3:
        print("转出账户的余额不足")
    elif num3==0:
        info = '''
                                           ------------个人信息------------
                                           用户名:%s               
                                           密码：*****
                                           余额：%s
                                           开户行名称：%s
                                       '''
        # 每个元素都可传入%
        print(info % (zhuanchuname, bank[zhuanchuname]["money"], bank_name))
        info = '''
                                           ------------个人信息------------
                                           用户名:%s               
                                           密码：*****
                                           余额：%s
                                           开户行名称：%s
                                       '''
        # 每个元素都可传入%
        print(info % (zhuanruname, bank[zhuanruname]["money"], bank_name))

def chaxunadd():
    name = input("请输入您的姓名：")
    password = int(input("请输入您的用户密码："))
    num4 = cxadd(name, password)

    if num4==1:
        print("账户信息不存在")
    elif num4==2:
        print("密码输入错误")
    elif num4==0:
        info = '''
                          ------------个人信息------------
                          用户名:%s
                          账号：%s
                          密码：%s
                          国籍：%s
                          省份：%s
                          街道：%s
                          门牌号：%s
                          余额：%s
                          开户行名称：%s
                      '''
        # 每个元素都可传入%

        print(info % (name, bank[name]['account'], bank[name]['password'],bank[name]['country'], bank[name]['province'],bank[name]['steert'], bank[name]['door'], bank[name]["money"], bank_name))



while False==0:
    index=int(input("请输入您需要的业务"))
    if index ==1:
        print("开户")
        useradd()
        print(bank)
    elif index ==2:
        print("存钱")
        cunqianadd()
    elif index ==3:
        print("取钱")
        quxianadd()
    elif index ==4:
        print("转账")
        zhuanzhangadd()
    elif index ==5:
        print("查询")
        chaxunadd()
    elif index ==6:
        print("下次光临")
        break
