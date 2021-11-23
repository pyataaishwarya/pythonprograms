#!/bin/python

def number_of_digits(n):
    i=1
    if (n==0):
        return 1
    while (n!=0):
        rem=n%10
        n=n//10
        i=i+1
    return i-1
n=eval(input("enter number to find number of digts in it"))
print("number of digits:%d" %(number_of_digits(n)))
#number_of_digits(n)

