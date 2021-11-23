#!/bin/python

def no_of_days_month(y,m):
    if (m==2):
        if (((y%4==0)and(y%100!=0))or((y%100==0)and(y%400==0))):
            return 29
        return 28
    if(m==4 or m==6 or m==9 or m==10):
        return 30
    if(m==1 or m==3 or m==5 or m==7 or m==8 or m==11 or m==12):
        return 31
y=eval(input("enter year"))
m=eval(input("enter month"))
d=no_of_days_month(y,m)
print("the number of days present in month %d is %d" %(m,d))




