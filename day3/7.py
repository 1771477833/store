#编程实现下列图形的打印
a=int(input("请输入层数："))
for i in range(a):
    print(" "*(a-1-i)+'*'*(i+1)+'*'*i)