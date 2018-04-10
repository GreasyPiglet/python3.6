设置Sublime Text的语法为python 
View -> syntax ->python
设置编译环境(默认python版本2.7) 
Tools -> Build System -> Python

************ 添加编译环境python3.6 **********

Sublime没有帮我们配置python3, 用python3的同学需要自己配置 

Tools -> Build System -> New Build System 

在打开的文件里面贴上以下代码: 

这个路径是你的python路径: /Library/Frameworks/Python.framework/Versions/3.5/bin/python3 

如果不是, 请换成你的python3路径

{
      "cmd": ["/Library/Frameworks/Python.framework/Versions/3.5/bin/python3", "-u", "$file"],
      "file_regex": "^[ ]*File \"(...*?)\", line ([0-9]*)",
      "selector": "source.python"
}