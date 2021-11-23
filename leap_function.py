#!/bin/python

def leap_or_not(y):
    if (((y%4==0)and(y%100!=0))or((y%100==0)and(y%400==0))):
        return 1
    else:
        return 0
y=eval(input("enter year"))
y1=leap_or_not(y)
if(y1==1):
    print("year",y,"is leap year")
else:
    print("year",y,"is not leap year")

