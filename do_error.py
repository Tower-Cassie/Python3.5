#!/Users/xiaohong/Desktop/Python3.5
#Filename:do_error.py
#_*_ coding:utf-8 _*_


#高级语言通常都内置了一套try...except...finally...的错误处理机制，Python也不例外。
try:
    print("try...")
    r = 10/0
    print("result:",r)
except ZeroDivisionError as e:
    print("except:",e)
finally:
    print("finally")
print("END\n")
#当我们认为某些代码可能会出错时，就可以用try来运行这段代码，如果执行出错，则后续代码不会继续执行，而是直接跳转至错误处理代码，即except语句块，执行完except后，如果有finally语句块，则执行finally语句块，至此，执行完毕。
#若没有错误发生，所以except语句块不会被执行，但是finally如果有，则一定会被执行（可以没有finally语句）


try:
    print("try...")
    r = 10/int('a')
    print("result:",r)
except ValueError as e:
    print("ValueError:",e)
except ZeroDivisionError as e:
    print("ZeroDivisionError:",e)
else:
    print("no error!")
finally:
    print("finally...")
print("END\n")



def foo():
    r = input("Please enter a num:")
    try:
        res = 10/int(r)
    except ZeroDivisionError as e:
        print("ZeroDivisionError:",e)
try:
    foo()
except ValueError as e:
    print("ValueError")
except UnicodeError as e:
    print("UnicodeError")
#第二个except永远也捕获不到UnicodeError，因为UnicodeError是ValueError的子类，如果有，也被第一个except给捕获了。


def foo(s):
    return 10/int(s)

def bar(s):
    return foo(s)  * 2

def main():
    try:
        bar('0')
    except Exception as e:
        print("Error:",e)
    finally:
        print("finally")

#也就是说，不需要在每个可能出错的地方去捕获错误，只要在合适的层次去捕获错误就可以了。这样一来，就大大减少了写try...except...finally的麻烦
main()

#Python内置的logging模块可以非常容易地记录错误信息：
#通过配置，logging还可以把错误记录到日志文件里，方便事后排查
import logging
def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)
main()
print("END\n")


#既然我们能捕获错误，就可以把错误堆栈打印出来，然后分析错误原因，同时，让程序继续执行下去。
def foo(s):
    res = int(s)
    if res == 0:
        raise ValueError("invalid value:%s"%s)
    return 10/n
def bar():
    try:
        foo('0')
    except ValueError as e:
        print("ValueError!")
        raise

bar()


#其实这种错误处理方式不但没病，而且相当常见。捕获错误目的只是记录一下，便于后续追踪。但是，由于当前函数不知道应该怎么处理该错误，所以，最恰当的方式是继续往上抛，让顶层调用者去处理。好比一个员工处理不了一个问题时，就把问题抛给他的老板，如果他的老板也处理不了，就一直往上抛，最终会抛给CEO去处理。
#raise语句如果不带参数，就会把当前错误原样抛出。此外，在except中raise一个Error，还可以把一种类型的错误转化成另一种类型

try:
    10/0
except ZeroDivisionError:
    raise ValueError("input error!")#只要是合理的转换逻辑就可以，但是，决不应该把一个IOError转换成毫不相干的ValueError



