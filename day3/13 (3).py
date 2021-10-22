n=int(input("请输入："))
i=1
j=1
while i<=n:
    for j in range(1,i+1):
        print("%d*%d=%2d\t"%(j,i,i*j),end='')
    print()
    i=i+1
print()
