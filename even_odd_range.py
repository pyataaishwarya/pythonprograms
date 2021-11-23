#!/bin/python

'''
n1=eval(input("enter the starting range of number"))
n2=eval(input("enter the ending range of number"))
i=n1

while(i<=n2):
    if (i%2==0):
        print("%d" %i)
    i=i+1
i=n1
print("odd numbers in given range")
while(i<=n2):
    if (i%2!=0):
        print("%d" %i)
    i=i+1
'''
def even_numbers(n1,n2):
    i=n1
    while (i<=n2):
        if (i%2==0):
            print("%d" %i)
        i=i+1
def odd_numbers(n1,n2):
    i=n1
    while (i<=n2):
        if (i%2!=0):
            print("%d" %i)
        i=i+1
n1=eval(input("enter the starting range of number"))
n2=eval(input("enter the ending range of number"))
print("even numbers in given range")
even_numbers(n1,n2)
print("odd numbers in given range")
odd_numbers(n1,n2)

