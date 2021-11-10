'''
    需求：
        抢票：
        500，刘备，张飞，关羽，同时抢票，看最后谁抢的多。
'''
import time
from threading import Thread
# 全局票池
sum = 0
money=0



class Person(Thread):
    username  = ""
    many = 0

    def run(self) -> None:
        while True:
            global sum
            global money
            if sum < 500:
                self.many = self.many + 1
                sum = sum + 1
                money = money + 3
                print("嘻嘻！",self.username,"成功制作了一个蛋糕，总共有",sum,"个蛋糕")
            elif sum==500:
                print(self.username, "总共制作了", self.many, "个蛋糕")

                time.sleep(3)
                continue
            elif money>=29988:
                print(self.username, "共收获了", self.many * 2.5, "块钱")
                break




class people(Thread):
    username1 = ""
    money = 5000
    many1=0

    def run(self) -> None:
        while True:
            global sum
            if sum==0:
                time.sleep(4)
            elif sum>0:
                self.money=self.money-3
                sum=sum-1
                self.many1=self.many1+1
                print("giegie",self.username1,"成功抢夺了一个蛋糕，还有",sum,"个蛋糕")
                print(self.username1,"吃了",self.many1,"个蛋糕")
                continue
            if self.money<=0:
                break








p1 = Person()
p2 = Person()
p3 = Person()

p1.username = "张飞"
p2.username = "关羽"
p3.username = "刘备"

p1.start()
p2.start()
p3.start()

p4 = people()
p5 = people()
p6 = people()
p7 = people()
p8 = people()
p9 = people()

p4.username1 = "宋丽阳"
p5.username1 = "宋丽洋"
p6.username1 = "陈白玉"
p7.username1 = "陈柏宇"
p8.username1 = "李泽辉"
p9.username1 = "李泽厚"

p4.start()
p5.start()
p6.start()
p7.start()
p8.start()
p9.start()