#!/bin/python

m=eval(input("enter number of numbers"))
n=eval(input("enter the number"))
l=n
s=n
i=1
while (i<=m-1):
    n=eval(input("enter the number"))
    if (n>l):
        l=n
    if(n<s):
        s=n
    i=i+1
print("largest number:%d" %l)
print("smallest number:%d" %s)

