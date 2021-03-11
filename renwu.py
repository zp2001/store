#实现输入十个数，求和
'''
b = 0
sum = 0
while b<10:
    a = int(input("请输入数字:"))
    sum = a+sum
    b+=1
print("数字之和为：",sum)


#从键盘依次输入10个数，最后打印最大的数、10个数的和、和平均数。

b = 0
sum = 0
big = 0

while b<10:
    a = int(input("请输入数字:"))
    sum = a+sum
    if a>big:
        big = a
    b+=1
pingjun=sum/big
print("数字之和为：",sum)
print("最大数值为：",big)
print("平均值为：",pingjun)

#使用random模块，如何产生 50~150之间的数？
import random
num = random.randint(50,150)
print(num)

#从键盘输入任意三边，判断是否能形成三角形，若可以，则判断形成什么三角形（结果判断：等腰，等边，直角，普通，不能形成三角形。）
a=int(input("请输入第一个边长:"))
b=int(input("请输入第二个边长:"))
c=int(input("请输入第三个边长:"))

if a==b==c:
    print("等边三角形")
elif a+b>c and b+c>a and a+c>b:
    print("普通三角形")
elif a==b or b==c or c==a:
    print("等腰三角形")
elif a*a+b*b==c*c or b*b+c*c==a*a or a*a+c*c==b*b:
    print("直角三角形")
else:
    print("不构成三角形")

#有以下两个数，使用+，-号实现两个数的调换。
a=56
b=78
print("a=",a+22)
print("b=",b-22)

#实现登陆系统的三次密码输入错误锁定功能（用户名：root,密码：admin）
name = 'root'
passwd = 'admin'

a=name
b=passwd

c =0
d =0

e=0
while e<3:
    c = input("请输入账号:")
    d = input("请输入密码:")
    if c == a and d == a:
        print("正确")
    else:
        print("密码错误")
    e+=1
print("锁定")

#星号三角形
for i in range(8):
    for j in range(0, 10 - i):
        print(end=" ")
    for k in range(10 - i, 10):
        print("*", end=" ")
    print("")

#使用while循环实现99乘法表
a=1
b=1
while a<=9:
    while b<=a:
        print(a,"*",b,"=",a*b)
        b += 1
    print("\t")
    b=0
    a+=1

#倒叙99乘法表
a=9
b=9
while a>=1:
    while b>=a:
        print(a,"*",b,"=",a*b,end="\t")
        b -= 1
    print()
    b=9
    a-=1

a =20
sun = 3
moon = 2
day =0
while 1:
    a -=sun
    if a==0: break
    a +=moon
    day +=1
print(day)

#判断下列变量命名是否合法  char,Oax_li,fLul,BYTE,Cy%ty,$123,3_3 ,T_T
help("keywords")

#游戏
import random
import time
num = random.randint(0, 10)
gold=0
n=0
asd=20
print("您的初始资金为0")
while 1:
    n+=1
    a = int(input("请输入一个数字："))
    if num > a:
        print("你猜的数字小了")
    elif num < a:
        print("你猜的数字大了")
    elif num==a:
        print("你成功了")
        print("你猜了",n,"次")
        if n<3:
            gold+=200
            print("游戏结束，您的资金为",gold)
        else:
            print("资金不加不减")
        break
    if n==20:
        print("您已经猜了20次了系统需要休息一下")
        while 1:
            time.sleep(1)
            print("还有",asd,"秒")
            asd-=1
            if asd==0:
                break
    elif n==6:
        print("您已经猜了60次了系统锁定")
        while 1:
            time.sleep(1)'''























