#!/Users/xiaohong/Desktop/Python3.5
#Filename:do_bytesIO.py
#_*_ coding:utf-8 _*_


#StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO
from io import BytesIO
f = BytesIO()


#encode前面不是逗号，是字符串的一个属性
f.write("中文".encode("utf-8"))
print(f.getvalue())

from io import BytesIO
f = BytesIO(b"\xe4\xb8\xad\xe6\x96\x87")
print(f.read())
