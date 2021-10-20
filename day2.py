'''
猜字游戏：
需求：
1、猜的数字是系统产生的，不是自己定义的
2、键盘输入的   操作完填入：input（“提示”）
3、判断			操作完填入：if判断条件 elif 判断条件。。。。。。Else
4、循环			操作完填入：while 条件循环
#任务：开始金币有5个金币，每猜一次减一个为0就退出（or充钱）猜错3次也退出
'''
import random
randint = random.randint(10, 20)  # 随机生成数字的范围：int   []
print(randint)
i=3
n=5
while i>=1:
    print("你还有%d次机会"%i)
    print("您还有%d个金币"%n)
    num=int(input("请输入您猜的数字"))
    if num==randint:
        print("恭喜你猜对了")
        n=n+3
        randint = random.randint(10, 20)  # 随机生成数字的范围：int   []
        print(randint)
        continue
    elif num>randint:
        print("猜大了")
    elif num<randint:
        print("猜小了")
    else:
        print("猜错了,继续猜")
    i=i-1
    n=n-1
print("您还剩余%d个金币"%n)

'''
import  random
a=int(random.random()*20)
n=3
m=5
print(a)
while n>1:
        for i in range(0,100):
            b=int(input("请输入您猜的数字:"))
            if b<a:
                print("大了")
                n=n-1
                m=m-1
            elif b>a:
                print("小了")
                n=n-1
                m=m-1
            else:
                print("对了")
                a = int(random.random() * 100)
                print(a)
                m=m+3
                continue
            if n<1:
                break
print("你剩余的金币为%d"%m)
'''


