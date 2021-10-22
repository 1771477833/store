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
    if i<1:
        print("机会已用光是否用金币换取机会")
        b=input()
        a='是' 

        if a==b:
            e = (n + i) /2
            print("您最多可以兑换%d个金币" % e)
            c=int(input("请输入兑换的金币"))
            if n>=c and n>=i:
                i=c
                n=n-c
                print("充值成功")
            else:
                print("余额不足")

        else:
            break


print("您还剩余%d个金币"%n)