#!/Users/xiaohong/Desktop/Python3.5
#Filename:do_stringIO.py
#_*_ coding:utf-8 _*_

from io import StringIO

#import io
#不能通过该引入进行导入StringIO,会报错

#write to StringIO
f = StringIO()
f.write("hello")
f.write(" ")
f.write("world!")


print(f.getvalue())


#read from StringIO
#要读取StringIO，可以用一个str初始化StringIO，然后，像读文件一样读取：
f = StringIO("水面细风生,\n菱歌慢慢声。\n客亭临小市，\n灯火夜妆明。")
while True:
    s = f.readline()
    if s == "":
        break
    print(s.strip())

