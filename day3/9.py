#一只青蛙掉在井里了，井高20米，青蛙白天网上爬3米，晚上下滑2米，问第几天能出来？请编程求出。
h=20
t=1
while True:
    if 3*t-2*(t-1)==20:
        break
    elif 3*t-2*t==20:
        break
    t=t+1
print("第%d天出来"%t)