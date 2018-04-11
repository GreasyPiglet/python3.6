print("你好")

# 1.注释 **********************
# 单行注释 -------

'''
（多行注释）
这里是多行注释1
这里是多行注释2
这里是多行注释3
'''

"""
（这也是多行注释）
这里是多行注释4
这里是多行注释5
这里是多行注释6
"""

# 2.注释 **********************



'''
行与缩进
python最具特色的就是使用缩进来表示代码块，不需要使用大括号 {} 。
缩进的空格数是可变的，但是同一个代码块的语句必须包含相同的缩进空格数。
缩进不一致，会导致运行错误。实例如下：
'''

if True:
	print("正确")
else: 
	print("错误")

'''
Python 通常是一行写完一条语句，但如果语句很长，我们可以使用反斜杠(\)来实现多行语句
'''

total = ['1','2','3',
		]
print(total)


# 字符串(String)
#python中单引号和双引号使用完全相同。
#使用三引号('''或""")可以指定一个多行字符串。
#转义符 '\'
#反斜杠可以用来转义，使用r可以让反斜杠不发生转义。。 如 r"this is a line with \n" 则\n会显示，并不是换行。
#按字面意义级联字符串，如"this " "is " "string"会被自动转换为this is string。
#字符串可以用 + 运算符连接在一起，用 * 运算符重复。
#Python 中的字符串有两种索引方式，从左往右以 0 开始，从右往左以 -1 开始。
#Python中的字符串不能改变。
#Python 没有单独的字符类型，一个字符就是长度为 1 的字符串。
#字符串的截取的语法格式如下：变量[头下标:尾下标]


print(r"r可以后面换行符不会转义\n，直接被打印")

name = 'zhangdi'
print(name)
print(name[0:-1]) # 输出第一个到倒数第二个的所有字符
print(name[0])
print(name[-1])
print(name[2:5])
print(name[2:])
print(name * 2)             # 输出字符串两次
print(name + '你好')        # 连接字符串
print('---------------')
print('ni\nhao')
print(r'ni\nhao')






