class cook:
    __name = ""
    __age = 0

    def setcookname(self, name):
        if len(name) > 4 and len(name) <= 1:
            print("姓名错误")
        else:
            self.__name = name

    def getcookname(self):
        return self.__name

    def setage(self, age):
        if age > 65 and age < 30:
            print("错误")
        else:
            self.__age = age

    def getage(self):
        return self.__age

    def steam(self, name):
        print("这个", self.__age, "岁名叫", self.__name, "的厨师正在蒸", name)


class son(cook):

    def steam(self, name):
        super().steam(name)

    def fry(self, name):
        print("炒", name)


class grandson(son):
    def steam(self, name):
        super().steam(name)

    def fry(self, name):
        super().fry(name)

cook = grandson()
cook.setcookname("张三")
cook.setage(40)
cook.steam("米饭")
cook.fry("白菜")
print(cook.getage(), cook.getcookname())
