#!/Users/xiaohong/Desktop/Python3.5
#Filename:class_attr.py
#_*_ coding:utf-8 _*_

#由于Python是动态语言，根据类创建的实例可以任意绑定属性。
#给实例绑定属性的方法是通过实例变量，或者通过self变量：
class Student(object):
    def __init__(self,name):
        self.name = name
        #此处的name是一个类属性，一旦加载类，这个属性就存在了
   
        
stu = Student("Bob")
stu.score = 90

print(stu.name)

class Student(object):
    name = "Student"

#如果要不传任何参数进行构建对象，则不能在类中定义任何其他带参的构造器  
stu1 = Student()
print(stu1.name)
stu1.name = "Cassie"
print(stu1.name)
print(Student.name)

del stu1.name
print(stu1.name)
print(Student.name)
#从上面的例子可以看出，在编写程序的时候，千万不要把实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性，但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性



