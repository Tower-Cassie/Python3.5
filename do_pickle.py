#!/Users/xiaohong/Desktop/Python3.5
#Filename:do_pickle.py
#_*_ coding:utf-8 _*_

#序列化
#我们把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，在其他语言中也被称之为serialization，marshalling，flattening等等，都是一个意思。
#序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。
#反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。

import pickle

#序列化
d = dict(name = "Bob",age = 12,score = 43)
print(pickle.dumps(d))


#pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object：
f = open("D:/icon.jpg","wb")
d = dict(name = "Bob",age = 12,score = 123)
pickle.dump(d,f)
f.close()


#当我们要把对象从磁盘读到内存时，可以先把内容读到一个bytes，然后用pickle.loads()方法反序列化出对象，也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象。我们打开另一个Python命令行来反序列化刚才保存的对象：
f = open("D:/a.txt","rb")
d = pickle.load(f)
f.close()
print(d)


#变量的内容又回来了！
#当然，这个变量和原来的变量是完全不相干的对象，它们只是内容相同而已。
#Pickle的问题和所有其他编程语言特有的序列化问题一样，就是它只能用于Python，并且可能不同版本的Python彼此都不兼容，因此，只能用Pickle保存那些不重要的数据，不能成功地反序列化也没关系。

#JSON
#如果我们要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式，比如XML，但更好的方法是序列化为JSON，因为JSON表示出来就是一个字符串，可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输。JSON不仅是标准格式，并且比XML更快，而且可以直接在Web页面中读取，非常方便。
#JSON表示的对象就是标准的JavaScript语言的对象，JSON和Python内置的数据类型对应如下：
#JSON类型	Python类型
#{}	        dict
#[]	        list
#"string"	str
#1234.56	int或float
#true/false	True/False
#null	        None


#Python内置的json模块提供了非常完善的Python对象到JSON格式的转换。我们先看看如何把Python对象变成一个JSON：
import json
d = dict(name = "Bob",age = 112,score = 123)
print(json.dumps(d))

json_str = '{"age" : 1112,"score":124,"name" : "Bob"}'
print(json.loads(json_str))


#JSON进阶
class Student(object):
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score
stu = Student("Cassie",12,120)
def stu2json(stu):
    return{
        "name":stu.name,
        "age":stu.age,#此处的逗号不能省略
        "score":stu.score
        }
    
#print(json.dumps(stu))
#前面的代码之所以无法把Student类实例序列化为JSON，是因为默认情况下，dumps()方法不知道如何将Student实例变为一个JSON的{}对象。
#可选参数default就是把任意一个对象变成一个可序列为JSON的对象，我们只需要为Student专门写一个转换函数，再把函数传进去即可：
print(json.dumps(stu,default = stu2json))

#下次如果遇到一个Teacher类的实例，照样无法序列化为JSON。我们可以偷个懒，把任意class的实例变为dict：
print(json.dumps(stu,default = lambda obj :obj.__dict__))

#因为通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。也有少数例外，比如定义了__slots__的class。
#同样的道理，如果我们要把JSON反序列化为一个Student对象实例，loads()方法首先转换出一个dict对象，然后，我们传入的object_hook函数负责把dict转换为Student实例
def json2student(js):
    return Student(js["name"],js["age"],js["score"])
print(json.loads(json_str,object_hook = json2student))
                 
      
