import time
class kongtiao:
    __pinpai = ""
    __money = 0.0


    def setpinpai(self, pinpai):
        if pinpai !="海尔" and pinpai != "格力":
            print("材料信息错误！")
        else:
            self.__pinpai = pinpai

    def getpinpai(self):
        return self.__pinpai

    def setmoney(self, money):
        if money < 200 or money > 5000:
            print("价格描述有误")
        else:
            self.__money = money

    def getmoney(self):
        return self.__money

    def kaiji(self):
        print("空调开机了！")

    def visit(self,hour):
        print("【温馨提示", end="")
        for i in range(3):
            print(".", end="")
            time.sleep(1)
        print("】空调将在",hour,"分钟后自动关闭")



    def showtime(self):
        print("空调的品牌为：",self.__pinpai,"价格为:",self.__money)

p=kongtiao()
p.setpinpai("格力")
p.setmoney(999)
p.kaiji()
p.visit(2)
p.showtime()