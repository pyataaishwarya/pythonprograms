#!/bin/python

def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def remainder(a,b):
    return a%b
def quotient(a,b):
    return a/b
def floordivision(a,b):
    return a//b
def power(a,b):
    return a**b
a=eval(input("enter a value"))
b=eval(input("enter b value"))
print("add:%d" %(addition(a,b)))
print("sub:%d" %(subtraction(a,b)))
print("mul:%d" %(multiplication(a,b)))
print("rem:%d" %(remainder(a,b)))
print("quo:%d" %(quotient(a,b)))
print("floordiv:%d" %(floordivision(a,b)))
print("power:%d" %(power(a,b)))

