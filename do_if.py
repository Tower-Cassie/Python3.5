#!/Users/xiaohong/Desktop/Python3.5
#Filename:do_if.py
#_*_ coding:utf-8 _*_

cnt = 1
while cnt <= 3:
    #The input data is String not num,so the number must be converted
    num = input("Please enter your age:")
    age = int(num)
    if age >= 18:
        print("adult")
        #elif is equal to (else and if)
    elif age >= 6:
        print("teenager")
    else:
        print("kids")
    cnt = cnt + 1


#test Sample
cnt = 1
while cnt <= 3:
    num1 = input("Please enter your height:")
    height = float(num1)
    num2 = input("Please enter your weight:")
    weight = float(num2)
    BMI = weight/(height * height)
    if BMI > 32:
        print ("严重肥胖")
    elif BMI >= 28:
        print("肥胖")
    elif BMI >= 25:
        ptint("过重")
    elif BMI >= 18.5:
        print("正常")
    else:
        print("过轻")
    cnt = cnt + 1
