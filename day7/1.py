''''
xlrd 调用表格读取
xlwt 写
'''
import xlrd

#1、通过xlr打开表格
table=xlrd.open_workbook(filename="2020年每个月的销售情况.xlsx",encoding_override=True)
#获取选项卡

#st=table.sheet_by_name("1月")
sum=0
n=0
while n<12:
    st=table.sheet_by_index(n)

    a=1
    yu=0
    niuzai=0
    fengyi=0
    picao=0
    Txue=0
    xiaoxizhuang=0
    piyi=0
    majia=0
    while a<len(st.col_values(0)):
        cell = st.cell(a, 1).value
        if cell=="羽绒服":
            yu=(st.cell(a, 2).value)*(st.cell(a, 4).value)+yu
        elif cell=="牛仔裤":
            niuzai = (st.cell(a, 2).value) * (st.cell(a, 4).value) + niuzai
        elif cell=="风衣":
            fengyi = (st.cell(a, 2).value) * (st.cell(a, 4).value) + fengyi
        elif cell == "皮草":
            picao = (st.cell(a, 2).value) * (st.cell(a, 4).value) + picao
        elif cell == "T血":
            Txue = (st.cell(a, 2).value) * (st.cell(a, 4).value) + Txue
        elif cell == "小西装":
            xiaoxizhuang = (st.cell(a, 2).value) * (st.cell(a, 4).value) + xiaoxizhuang
        elif cell == "皮衣":
            piyi = (st.cell(a, 2).value) * (st.cell(a, 4).value) + piyi
        elif cell == "马甲":
            majia = (st.cell(a, 2).value) * (st.cell(a, 4).value) + majia
        sum=yu+niuzai+fengyi+picao+Txue+xiaoxizhuang+piyi+majia+sum


        a=a+1

    n=n+1
#统计年龄的总和
print("总销售金额为:%d"%sum)
#sum（）求和
#   切片[开始角标，结束角标，跳跃]