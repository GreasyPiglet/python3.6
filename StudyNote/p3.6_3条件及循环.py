#!/usr/bin/env python3

print('斐波那契数列')

a, b = 0, 1

while b < 100 :
	print(b, end=',')
	a, b = b, a+b


n = int(input('亲，输入一个正整数：'))

def fab(n):
	if n<1:
		print('亲，输入的不对哦')
		return -1
	if n==1 or n==2:
		return 1
	else: 
		return fab(n-1)+fab(n-2)

result = []
for i in range(1,n+1):
	result.append(fab(i))

print(result)