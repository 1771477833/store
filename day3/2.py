#从键盘依次输入10个数，最后打印最大的数、10个数的和、和平均数。
list=[]
print(len(list))
for b in range(0,10,+1):
    a=int(input("请输入："))
    list.append(a)
print(list)
sum=0
best=0
for i in range(len(list)):# i == 0,1,2,3,4,5
    sum=int(list[i])+sum
    print("第%d个数字为"%(i+1),list[i])
for i in range(len(list)):
    if best<int(list[i]):
        best=int(list[i])
    elif best>=int(list[i]):
        continue
average=sum/(len(list))
print("最大值为：%d"%best)
print("求和值为：%d"%sum)
print("平均数为：%d"%average)