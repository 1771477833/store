b=open(file="baidu_x_system.log",mode="r+")
data=b.readlines()
list=[]
i=0
j=0
a=['1', '0', '.', '1', '5', '5', '.', '2', '4', '.', '1', '3', '2']
a1=0
b=['1', '6', '.', '1', '5', '5', '.', '3', '4', '.', '1', '3', '2']
b1=0
c=['5', '6', '.', '7', '8', '.', '3', '5', '.', '1', '3', '1',' ']
c1=0
d=['4', '6', '.', '7', '6', '.', '1', '8', '5', '.', '3', '6',' ']
d1=0
list1=[]

while i<32:
    list = []
    while j<13:

        list.append(data[i][j])
        j = j + 1
        if j == 13:

            if list not in list1:


                list1.append(list)
            elif list in list1:

                if list==a:
                    a1=a1+1
                elif list==b:
                    b1=b1+1
                elif list == c:
                    c1 = c1 + 1
                elif list == d:
                    d1 = d1 + 1







    i = i + 1
    j=0

print("10.155.24.132ip地址相同的地址共有",a1+1,"个")
print("16.155.34.132ip地址相同的地址共有",b1+1,"个")
print("56.78.35.131ip地址相同的地址共有",c1+1,"个")
print("46.76.185.36ip地址相同的地址共有",d1+1,"个")