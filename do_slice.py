#!/Users/xiaohong/Desktop/Python3.5
#Filename:do_for.py
#_*_ coding:utf-8 _*_

#字符串，序列和元组都可以实现切片操作，只是元组和字符串都是不可变对象
list = [1]
num = 3
while num <= 99:
    list.append(num)
    num = num + 2
print("The whole elements of list is:\n%s\n"%list)


#取列表中的前一半元素
print ("The half elements of list is:\n",list[:25])

#取前面三个数
print("The three elements in the front is:\n",list[:3])

#取后面三个数
print("The three elements in the behind is:\n",list[-3:])

#取11-20个数
print("The elements at 11 - 20  is:\n",list[11:20])

#前面10个数中，每两个取一个
print("The elemenrs is:\n",list[:10:2])

#所有数中，每5个取一个
print("The elements is:\n",list[::5])


str = "ADFAKFLJFL;"
#输出前三个字符
print(str[:3])


tuple = (1,2,3,4)
#输出前三个字符
print(tuple[:3])
