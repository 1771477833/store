# 姓名  年龄  性别  编号   任职公司   薪资   部门编号
names = [
    ["曹操","56","男","106","IBM", 500 ,"50"],
    ["大乔","19","女","230","微软", 501 ,"60"],
    ["小乔", "19", "女", "210", "Oracle", 600, "60"],
    ["许褚", "45", "男", "230", "Tencent", 700 , "10"]
]


i=0
sum=0
while i<4:
    print(int(names[i][5]))
    sum=int(names[i][5])+sum
    i=i+1

a=sum/i
print("每个人的平均薪资为：%d"%a)