''''
xlrd 调用表格读取
xlwt 写
'''
import xlrd

#1、通过xlr打开表格
table=xlrd.open_workbook(filename="2020年每个月的销售情况.xlsx",encoding_override=True)
#获取选项卡

#st=table.sheet_by_name("1月")
day=0
n=0
sum=0
while n<12:
    st=table.sheet_by_index(n)

    a=1
    while a<len(st.col_values(0)):
        cell = st.cell(a, 4).value
        sum=cell+sum




        a=a+1
    day = len(st.col_values(0))+day
    n=n+1
#统计年龄的总和
aug=sum/day
print("平均每日的销售量为:%d"%aug)
#sum（）求和
#   切片[开始角标，结束角标，跳跃]