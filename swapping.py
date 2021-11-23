#!/bin/python

def swap(a,b):
    a,b=b,a
    return a,b
a=eval(input("enter value of a:"))
b=eval(input("enter value of b:"))
print("before swapping a:%d b:%d" %(a,b))
print("after swapping a:%d b:%d" %(swap(a,b)))

'''
def swap(a,b):
    temp=a
    a=b
    b=temp
    return a,b
a,b=[eval(x) for x in input("enter the numbers").split()]
print("the numbers before swapping a=%d\tb=%d" %(a,b))
print("the numbers after swapping a=%d\tb=%d" %(swap(a,b)))

'''
print("end")
