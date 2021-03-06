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

"""
函数之间或类的方法之间用空行分隔，表示一段新的代码的开始。类和函数入口之间也用一行空行分隔，以突出函数入口的开始。
空行与代码缩进不同，空行并不是Python语法的一部分。书写时不插入空行，Python解释器运行也不会出错。但是空行的作用在于分隔两段不同功能或含义的代码，便于日后代码的维护或重构。
记住：空行也是程序代码的一部分。
"""


# 等待用户输入
# input('\n输入Enter退出')

#同一行显示多条语句
import sys;x = 'zhangdi';sys.stdout.write(x + 'x'+'\n')


#print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 end=""：

str1 = 'a'
str2 = 'm'

#换行输出
print(str1)
print(str2)

#不换行输出
print(str1,end=" ")
print(str2)


'''
import 与 from...import
在 python 用 import 或者 from...import 来导入相应的模块。
将整个模块(somemodule)导入，格式为： import somemodule
从某个模块中导入某个函数,格式为： from somemodule import somefunction
从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
将某个模块中的全部函数导入，格式为： from somemodule import *
'''

import sys
print('================Python import mode==========================')
print ('命令行参数为:')
for i in sys.argv:
    print (i)
print ('\n python 路径为',sys.path)


#导入 sys 模块的 argv,path 成员
from sys import argv,path  #  导入特定的成员
 
print('================python from import===================================')
print('path:',path) # 因为已经导入path成员，所以此处引用时不需要加sys.path
