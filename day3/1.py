#实现输入10个数字，并打印10个数的求和结果
list=[8,7,6,9,10,1, 2, 3, 4, 5]#列表是通过角标来获取值
#角标  0，  1，2， 3，4 ,5, 6
#长度减一就是角标的最大值
print(len(list))
# print(list[3])#读列表的值
# list.append("a")#添加到最后一个
# list.insert(1,"b")#指定添加到某个角标
# num1=list.remove(2)#通过值来删除
# num=list.pop()#默认弹出最后一个,是可以赋值的
print(list)
#这是第一种遍历列表的内容，不推荐这样写
# for i in list:
#     print(i)
#         数数   0,7 0~6 range[)
sum=0
for i in range(len(list)):# i == 0,1,2,3,4,5#     in后面计算的表达式结果赋值给i
    sum=int(list[i])+sum

    print("第%d个数字为"%(i+1),list[i])
    print("求和值为：%d"%sum)