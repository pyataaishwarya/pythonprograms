#!/bin/python

def prime_or_not(n):
    if (n>1):
        for i in range(2,int(n/2)+1):
            if(n%i==0):
                return 1
                break
        else:
            return 0
    else:
        return 1

n=eval(input("enter the number"))
n1=prime_or_not(n)
if(n1==1):
    print("number",n,"is not prime")
else:
    print("number",n,"is prime")

'''
def prime_or_not(n):
    if (n>1):
        for i in range(2,int(n/2)+1):
            if (n%i==0):
                print("number is not prime:%d" %n)
                break
        else:
            print("number is prime:%d" %n)
    else:
        print("number is not prime:%d" %n)
n=eval(input("enter the number"))
prime_or_not(n)
'''
