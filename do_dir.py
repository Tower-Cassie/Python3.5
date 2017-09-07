#!/Users/xiaohong/Desktop/Python3.5
#Filename:do_dir.py
#_*_ coding:utf-8 _*_


import os
#如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统
print(os.name)

#注意uname()函数在Windows上不提供，也就是说，os模块的某些函数是跟操作系统相关的
#print(os.uname())

#在操作系统中定义的环境变量，全部保存在os.environ这个变量中，可以直接查看：
#print(os.environ)

#要获取某个环境变量的值，可以调用os.environ.get('key')：
#print(os.environ.get("PATH"))

print(os.environ.get("x","default"))


#操作文件和目录

#查看当前目录的绝对路径
print(os.path.abspath("."))

#在某个目录下创建一个新目录，首先要把新目录的完整路径表示出来
os.path.join("D:","testdir")

#创建一个新目录
os.mkdir("D:/testdir")

#删除一个目录
os.rmdir("D:/testdir")

#把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符。在Linux/Unix/Mac下，os.path.join()返回这样的字符串
#同样的道理，要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：
print(os.path.split("/Users/xiaohong/AppData/Local/Adobe"))


#os.path.splitext()可以直接让你得到文件扩展名，很多时候非常方便：
print(os.path.splitext("D;/a.txt"))

#这些合并、拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作。
#文件操作使用下面的函数。假定当前目录下有一个test.txt文件：
#os.rename("test.txt","test.py")
#os.remove("test.py")


#最后看看如何利用Python的特性来过滤文件。比如我们要列出当前目录下的所有目录，只需要一行代码：
print([x for x in os.listdir(".") if os.path.isdir(x)])

#要列出所有的.py文件，也只需一行代码：
print([x for x in os.listdir(".") if os.path.isfile(x)  and os.path.splitext(x)[1] == ".py"])

#编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。
import os
def file_find(path,value):
    for x in os.listdir("."):#遍历目录
        if os.path.isdir(x):#如果是目录，则递归调用
            file_find(os.path.join(path,x),value)
        elif os.path.basename(x).find(value) != -1:#判断文件名是否包含所需查询的内容
            print(os.path.join(path,x))#打印路径
file_find("../Python3..5","py")
