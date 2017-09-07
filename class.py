#!/Users/xiaohong/Desktop/Python3.5
#Filename:call_func.py
#_*_ coding:utf-8 _*_

#面向过程的编程思想:命令的集合
stu1 = {"name":"Cassie","score":99}
stu2 = {"name":"Bob","score":42}

def print_score(stu):
    print("%s:%s"%(stu["name"],stu["score"]))

print_score(stu1)
print_score(stu2)



#面向对象的编程思想：对象的集合，先抽象出类，然后将类具体实例化
class Student(object):
    #此处的self不能删除，也不能替换成其他字符
    def __init__(self,name,score):
        self.name = name
        self.score = score

    def print_score(self):
        print("%s:%s"%(self.name,self.score))
    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return "B"
        else:
            return "C"

stu1 = Student("Cassie",54)
stu2 = Student("David",99) 

print("stu1.name =",stu1.name)
print("stu2.name =",stu2.name)
stu1.print_score()
stu2.print_score()

print("grade of stu1:",stu1.get_grade())
print("grade of stu2:",stu2.get_grade())

stu1.age = 2
print(stu1.age)



