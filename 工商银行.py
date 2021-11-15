from  工商银行完整版 import bank_addUser
from 工商银行完整版 import bank_saveMoney
from 工商银行完整版 import getRandom
from unittest import TestCase
from ddt import  ddt
from ddt import data
from ddt import unpack
import xlrd
import xlwt
from xlutils.copy import copy

# username,password,country,province,street,door,money
table=xlrd.open_workbook(filename="HKR.xlsx",encoding_override=True )
st = table.sheet_by_index(0)

a=1
list=[]
while a<len(st.col_values(0)):
    nol=st.row_values(a)

    list.append(nol)
    a=a+1
j=1
while j < len(st.col_values(0)):

    i=0
    while i <4:
        del list[j-1][8]
        i=i+1
    j=j+1
print(list)



@ddt
class TestBank(TestCase):
    @data(*list)
    @unpack
    def testAddUser(self,a,b,c,d,e,f,g,h):


        result = bank_addUser(a,b,c,d,e,f,g)
        z = 1
        wb = copy(table)
        ws = wb.get_sheet(0)
        while z < len(st.col_values(0)):

            if result != h:  # 将测试结果回写到excel表格中。
                ws.write(z, 8, "不通过！")
                wb.save("123.xlsx")

            else:
                ws.write(z, 8, "通过！")
                wb.save("123.xlsx")

            z=z+1

        self.assertEqual(result,h)


