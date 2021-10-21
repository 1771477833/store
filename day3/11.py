#用循环来实现20以内的数的阶乘。（1! +2!+3!+…..+20!）
num=1
sum=0
for i in range(1,20+1):
    num *=i
    sum=num+sum

    print(num)
print("\n")
print("20阶乘总和为:%d"%sum)