import time
class computer:
    __size = 0.0
    __money = 0.0
    __cpusize = ""
    __neicunsize = 0.0
    __daijitime=0.0

    def setsize(self, size):
        if size < 14 or size > 50:
            print("材料信息错误！")
        else:
            self.__size = size

    def getsize(self):
        return self.__size

    def setmoney(self, money):
        if money < 2000 :
            print("容积过大！")
        else:
            self.__money = money

    def getmoney(self):
        return self.__money

    def setcpusize(self, setcpusize):
        if setcpusize != "i3" and setcpusize != "i5" and setcpusize != "i7":
            print("与实体描述不符")
        else:
            self.__setcpusize = setcpusize

    def getsetcpusize(self):
        return self.__setcpusize

    def setneicunsize(self, neicunsize):
        if neicunsize<500:
            print("材质与实体不一致")
        else:
            self.__neicunsize=neicunsize

    def getneicunsize(self):
        return self.__neicunsize

    def setdaijitime(self, daijitime):
        if daijitime<0 or daijitime>24:
            print("材质与实体不一致")
        else:
            self.__daijitime=daijitime

    def getdaijitime(self):
        return self.__neicunsize

    def wirte(self,hour):
        print("我今天使用电脑打字",hour,"小时")

    def games(self,hour):
        print("我今天使用电脑打游戏",hour,"小时")

    def visit(self,hour):
        print("我今天使用电脑看视频",hour,"小时")
        print("【温馨提示", end="")
        for i in range(3):
            print(".", end="")
            time.sleep(1)
        print("】您的电脑即将关闭，请及时充电")



    def showtime(self):
        print("笔记本的屏幕大小为：",self.__size,"价格为:",self.__money,"cpu型号为：",self.__cpusize,"内村大小为:",self.__neicunsize,"超长待机",self.__daijitime,"小时")

p=computer()
p.setsize(15.6)
p.setmoney(9999)
p.setcpusize("i7")
p.setneicunsize(1000)
p.setdaijitime(12)

p.wirte(2)
p.games(8)
p.visit(2)
p.showtime()

