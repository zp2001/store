# #有一个列表，[“北京”,”上海”,”广东”]
# a = ["北京","上海","广东"]
# a.append("天津")
# a.append("重庆")
# a.append("哈尔滨")
# a.append("银川")
# a.append("郑州")
# a.append("济南")
# a.append("太原")
# a.append("合肥 ")
# a.append("长春")
# a.append("沈阳")
# a.append("呼和浩特 ")
# a.append("石家庄")
# a.append("乌鲁木齐")
# a.append("兰州")
# a.append("西宁")
# a.append("西安")
# a.append("长沙")
# a.append("武汉")
# a.append("南京")
# a.append("成都")
# a.append("贵阳")
#
# a.remove("广东")
# a.insert(1,"广东")
# print(a)
#
# a=[36710.36,35427.10,29863.23,29667.39,27665.36,27650.45,27620.38,25369.20]
# b=sum(a)
# svg=b/8
# print("gdp总和是：",b)
# print("gdp平均值是：",svg)
#
#
#求其中是5的倍数的和
# a = [1,5,21,30,15,9,30,24]
#
# b=0
# sum=0
# d=0
# while b<7:
#     c = a.pop()
#     if c %5 ==0:
#         d = c
#         sum = d + sum
#         b+=1
#     else:
#         b+=1
# print(sum)

#实现list = [9,8,7,6,5,4,3,2,1]
# List = [1,2,3,4,5,6,7,8,9]
# list2=[]
# List.reverse()
# for a in List:
#     list2.append(a)
# print(list2)

#统计每个数字出现的次数
List = [1,4,7,5,8,2,1,3,4,5,9,7,6,1,10]
# print(List.count(1))
# print(List.count(2))
# print(List.count(3))
# print(List.count(4))
# print(List.count(5))
# print(List.count(6))
# print(List.count(7))
# print(List.count(8))
# print(List.count(9))
# print(List.count(10))

c=1
while c<10:
    print(c,"出现的次数",List.count(c))
    c+=1















