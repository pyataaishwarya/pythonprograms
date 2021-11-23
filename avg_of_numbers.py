#!/bin/pyhon

def avg_of_nums(a,b,c,d):
    avg=(a+b+c+d)/4
    return avg
a,b,c,d=[eval(x) for x in input("enter four numbers to find avg").split()]
print("the average of numbers is %f"%(avg_of_nums(a,b,c,d)))


