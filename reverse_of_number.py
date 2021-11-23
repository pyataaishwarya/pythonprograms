#!/bin/python

def reverse_of_number(n):
    rev=0
    while (n>0):
        rem=n%10
        rev=rev*10+rem
        n=n//10
    print("reverse of number is %d" %rev)
n=eval(input("enter the number"))
reverse_of_number(n)

