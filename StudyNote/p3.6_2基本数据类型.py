#!/usr/bin/python3

counter = 100
miles = 34.0
name = '校长'
print(counter)
print(miles)
print(name)


#Number（数字）
#Python3 支持 int、float、bool、complex（复数)
a,b,c,d = 1,20.0, 4+3j, True
print(type(a),type(b),type(c),type(d))

#isinstance 判断类型
print(isinstance(a,str))

#type()不会认为子类是一种父类类型。
#isinstance()会认为子类是一种父类类型。
