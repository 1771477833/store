class shuibei:
    __high = 0.0
    __rongji = 0.0
    __color = ""
    __caizhi = ""

    def sethigh(self, high):
        if high < 0 or high > 1:
            print("材料信息错误！")
        else:
            self.__high = high

    def gethigh(self):
        return self.__high

    def setrongji(self, rongji):
        if rongji < 0 or rongji > 1:
            print("容积过大！")
        else:
            self.__rongji = rongji

    def getrongji(self):
        return self.__rongji

    def setcolor(self, color):
        if color != "黄色" and color != "黑色" and color != "白色" and color != "粉色" and color != "紫色" and color != "红色":
            print("与实体描述不符")
        else:
            self.__color = color

    def getcolor(self):
        return self.__color

    def setcaizhi(self, caizhi):
        if caizhi != "不锈钢" and caizhi != "塑料" and caizhi != "陶瓷":
            print("材质与实体不一致")
        else:
            self.__caizhi=caizhi

    def getcaizhi(self):
        return self.__caizhi

    def cun(self):
        print("能存放:", self.__rongji, "立方米液体", )

    def showtime(self):
        print("水杯的高度为：",self.__high,"水杯的材质为:",self.__caizhi,"水杯的容积为：",self.__rongji,"水杯的颜色为:",self.__color)

p=shuibei()
p.sethigh(0.55)
p.setcaizhi("不锈钢")
p.setrongji(0.4)
p.setcolor("白色")

p.cun()
p.showtime()
