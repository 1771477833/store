#从键盘输入任意三边，判断是否能形成三角形，若可以，则判断形成什么三角形（结果判断：等腰，等边，直角，普通，不能形成三角形。）
import  random
a=int(input("请输入a："))
b=int(input("请输入b："))
c=int(input("请输入c："))
print("a边长为%d："%a,"b边长为请输入%d："%b,"c边长为请输入%d："%c)

if a==b&a==c|b==a&b==c|c==a&c==b:
    print("该三角形为等腰三角形")
if a==b==c:
    print("该三角形为等边三角形")
if a*a==b*b+c*c|b*b==a*a+c*c|c*c==a*a+b*b:
    print("该三角形为直角三角形")
if a+b>c&a-b<c|b+c>a&b-c<a|a+c>b&a-c<b:
    print("该三角为普通三角形")
else:
    print("三边不能组成三角形")