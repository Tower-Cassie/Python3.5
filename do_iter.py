#!/Users/xiaohong/Desktop/Python3.5
#Filename:do_iter.py
#_*_ coding:utf-8 _*_


#Iterable是迭代对象，Iterator是迭代器
from collections import Iterable
print(isinstance([],Iterable))
print(isinstance({},Iterable))
print(isinstance((),Iterable))
print(isinstance("ask",Iterable))
print(isinstance((x for x in range(10)),Iterable))
print(isinstance(100,Iterable))
print()


from collections import Iterator
print(isinstance([],Iterator))
print(isinstance((),Iterator))
print(isinstance((x for x in range(10)),Iterator))
print()


print(isinstance(iter([]),Iterator))
print(isinstance(iter("sfh"),Iterator))
