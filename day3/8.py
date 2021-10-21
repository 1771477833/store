#编程实现99乘法表的倒叙打印
for i in range(9,0,-1):
    for j in range(1,i+1):
        print("%d*%d=%2d\t"%(j,i,i*j),end='')
    print()