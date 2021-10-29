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
            yu=(st.cell(a, 4).value)+yu
        elif cell=="牛仔裤":
            niuzai = (st.cell(a, 4).value) + niuzai
        elif cell=="风衣":
            fengyi = (st.cell(a, 4).value) + fengyi
        elif cell == "皮草":
            picao =  (st.cell(a, 4).value) + picao
        elif cell == "T血":
            Txue = (st.cell(a, 4).value) + Txue
        elif cell == "小西装":
            xiaoxizhuang =  (st.cell(a, 4).value) + xiaoxizhuang
        elif cell == "皮衣":
            piyi =  (st.cell(a, 4).value) + piyi
        elif cell == "马甲":
            majia = (st.cell(a, 4).value) + majia
        sum=yu+niuzai+fengyi+picao+Txue+xiaoxizhuang+piyi+majia

        a=a+1
    yu = yu / sum*100
    niuzai = niuzai / sum*100
    fengyi = fengyi / sum*100
    picao = picao / sum*100
    Txue = Txue / sum*100
    xiaoxizhuang = xiaoxizhuang / sum*100
    piyi = piyi / sum*100
    majia = majia / sum*100
    print(
        "第%d"%(n+1),"月羽绒服每月销售占比是：%d%%"%yu,"\n",
        "第%d" % (n + 1), "月牛仔裤每月销售占比是：%d%%" % niuzai,"\n",
        "第%d" % (n + 1), "月风衣每月销售占比是：%d%%" % fengyi,"\n",
        "第%d" % (n + 1), "月皮草每月销售占比是：%d%%" % picao,"\n",
        "第%d" % (n + 1), "月T血每月销售占比是：%d%%" % Txue,"\n",
        "第%d" % (n + 1), "月小西装每月销售占比是：%d%%" % xiaoxizhuang,"\n",
        "第%d" % (n + 1), "月皮衣每月销售占比是：%d%%" % piyi,"\n",
        "第%d" % (n + 1), "月马甲每月销售占比是：%d%%" % majia,"\n"

        )
    n=n+1

#统计年龄的总和

#sum（）求和
#   切片[开始角标，结束角标，跳跃]