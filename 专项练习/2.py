class student:
    __xuehao = ""
    __name = ""
    __age=0.0
    __sex=""
    __high=0.0
    __tizhong=0.0
    __chengji=0.0
    __zhuzhi=""
    __phone=""

    def setxuehao(self, xuehao):
        if len(xuehao) > 8:
            print("学号输入有误！")
        else:
            self.__xuehao = xuehao

    def getxuehao(self):
        return self.__xuehao

    def setname(self, name):
        if len(name) > 4:
            print("你是日本人么？")
        else:
            self.__name = name

    def getname(self):
        return self.__name

    def setage(self, age):
        if age > 100 or age < 0:
            print("你是地球人么？")
        else:
            self.__age = age

    def getage(self):
        return self.__age

    def setsex(self, sex):
        if sex != "男" and sex != "女":
            print("你是泰国人吗？？")
        else:
            self.__sex = sex

    def getsex(self):
        return self.__sex

    def sethigh(self, high):
        if high < 0 or high > 3:
            print("你是火星人？")
        else:
            self.__high = high

    def gethigh(self):
        return self.__high

    def settizhong(self, tizhong):
        if tizhong < 0 or tizhong > 200:
            print("厚礼蟹！")
        else:
            self.__tizhong = tizhong

    def gettizhong(self):
        return self.__tizhong

    def setchengji(self, chengji):
        if chengji < 0 or chengji > 100:
            print("你跟我俩开玩笑呢？？")
        else:
            self.__chengji = chengji

    def getchengji(self):
        return self.__chengji

    def setzhuzhi(self, zhuzhi):
        self.__zhuzhi = zhuzhi

    def getzhuzhi(self):
        return self.__zhuzhi

    def setphone(self, phone):
        if len(phone) < 11:
            print("???????？")
        else:
            self.__phone = phone

    def getphone(self):
        return self.__phone






    def xuexi(self,hour):
        print(self.__name,"今天学习了",hour,"小时")

    def game(self,gamesname):
        print("然后",self.__name,"玩了一款名叫",gamesname,"的游戏")

p=student()
p.sethigh=(1.95)
p.settizhong(95)
p.setsex("男")
p.setage(20)
p.setxuehao("200064")
p.setphone("13120121297")
p.setzhuzhi("北京市")
p.setchengji(99)
p.setname("孙鹏")
p.xuexi(2)
p.game("英雄联盟")
