#!/usr/bin/env python3

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
#
#
#

student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}

if ('ATom' in student):
     print('in')
else:
     print('no in')



A = set('许丽华是个好老婆')
B = set('许丽华个MM')
print(A)
print(A-B)
print(A|B)
print(A&B)
print(A^B)
