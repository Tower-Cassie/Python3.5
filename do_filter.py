#!/Users/xiaohong/Desktop/Python3.5
#Filename:do_filter.py
#_*_ coding:utf-8 _*_

#filter()函数和map类似，也是接收一个函数和一个序列，和map不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素
#filter这个高阶函数，关键在于正确实现一个筛选函数

#删调偶数，只保留奇数
def is_odd(n):
    return n %2 == 1
print(list(filter(is_odd,[1,2,3,4,5,6,7,8,9])))

#把一个序列中的空字符串删掉，可以这样写：
def not_empty(s):
    return s and s.strip()
print(list(filter(not_empty,['A','','B','','C'])))


#利用埃式筛选法进行素数的筛选
#先构造一个从3 开始的奇数序列
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def not_divisible(n):
    return lambda x: x % n > 0

def primes():#primes()是一个无限序列，所有调用时需要设置一个退出循环的条件
    yield 2#先返回第一个素数2，然后利用filter()不断产生删选后的新的序列
    it = _odd_iter()#初始序列
    while True:
        n = next(it)#返回序列的第一个数
        yield n
        it = filter(not_divisible(n),it)

for n in primes():
    if n < 10:
        print(n)
    else:
        break

#Sample example:测试一组序列是否时回数，回数是指从左向右读和从右向左读是一样的数
def is_palindrome(n):
    #实现字符串的翻转
    strm = str(n)[-1::-1]
    return strm == str(n)
print(list(filter(is_palindrome,range(1,1000))))
