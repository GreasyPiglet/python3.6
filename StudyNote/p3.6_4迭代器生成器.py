
#!/usr/bin/python3.6

# 迭代器
import sys


list = [1,2,3,4]
it = iter(list)

'''
for x in it:
	print(x, end="..")
'''
'''
while True:
	try:
		print(next(it))
	except StopIteration:
		sys.exit()
'''


def fibonacci(n):
	a,b,count = 0,1,0
	while True:
		if count>n:
			return
		yield a
		a,b = b,a+b
		count += 1


f = fibonacci(10)

while True:
	try:
		print(next(f),end=" ")
	except StopIteration:
		sys.exit()
