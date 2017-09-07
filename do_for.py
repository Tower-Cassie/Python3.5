#!/Users/xiaohong/Desktop/Python3.5
#Filename:do_for.py
#_*_ coding:utf-8 _*_

#Sum 1 - 100
sum = 0
for num in range(101):
    sum = sum + num
print (sum)

#Calgratuate the sum of odd
sum = 0
n = 99
while n > 0:
    sum = sum + n;
    n = n - 2
print (sum)

#Test Simple
List = ["Bart","Lisa","Adam"]
for temp in List:
    print ("Hello,",temp)

#break
n = 1
while n <= 99:
    if(n > 5):
        break;
    print (n)
    n = n + 1
print ("END")


#continue
#print odd
n = 0
while n < 10:
    n = n + 1
    if(n % 2== 0):
        continue;
    print(n)
print ("END")


   
