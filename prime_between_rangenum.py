#!/bin/python

def prime_between_range(n1,n2):
    if(n1>1):
        for i in range(n1,n2+1):
            for j in range(2,int(i/2)+1):
                if (i%j==0):
                    print("number is not prime %d" %i)
                    break
            else:
                print("number is prime %d" %i)
    else:
        print("number is not prime %d" %i)
n1=eval(input("enter the starting number"))
n2=eval(input("enter the ending number"))
prime_between_range(n1,n2)

