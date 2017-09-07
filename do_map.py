#!/Users/xiaohong/Desktop/Python3.5
#Filename:do_map.py
#_*_ coding:utf-8 _*_


def f(x):
    return x * x
#map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
#reduce把结果继续和序列的下一个元素做累积计算
res = map(f,[1,2,3,4,5])
print(list(res))

print(list(map(str,[1,2,3,4])))


from functools import reduce
#相当于做累加
def add(x,y):
    return x + y
print(reduce(add,[1,3,5,7]))


#相当于做累乘:将字符转换成对应整数
def fn(x,y):
    return x * 10 + y
print(reduce(fn,[1,2,3,4,5]))


def char2num(s):
    return {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}[s]
print(reduce(fn,map(char2num,"1234646")))


#整理成一个函数
def str2int(s):
    def fn(x,y):
        return x * 10 + y
    def char2num(s):
        return {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}[s]
    return reduce(fn,map(char2num,s))
print(str2int("451656"))


#Sample example1:把用户输入的不规范的英文名字，变为首写字母大写，其他小写的规范名字
def convert(name):
    return name.lower().capitalize()

#还可以这样实现字符的转换
def normalize(name):
    return name[:1].upper() + name[1:].lower()

List1 = ['adam','LISA','barT']
print(list(map(convert,List1)))

#Sample example2:可以接受一个list并利用reduce()求积
def prod(L):
    def muti(x,y):
        return x * y
    return reduce(muti,L)
print("3 * 5 * 7 * 9 =",prod([3,5,7,9]))

#Sample example3:将一个字符串转换成浮点数,将'132.56' 转换成132.56
def str2float(str1):
    def fn(x,y):
        return x * 10 + y
    def char2num(s):
        return {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}[s]
    list = str1.split('.')
    a = list[0]
    b = list[1]
    return reduce(fn,map(char2num,a)) + reduce(fn,map(char2num,b)) * 10 **(-len(b))
print(str2float("123.456"))
