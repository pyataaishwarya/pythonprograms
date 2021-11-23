#!/bin/python

from math import *
def area_perimeter(r,a,l,b):
    a_c=pi*r*r
    p_c=2*pi*r
    a_s=a*a
    p_s=4*a
    a_r=l*b
    p_r=2*(l+b)
    return a_c,p_c,a_s,p_s,a_r,p_r
r,a,l,b=[eval(x) for x in input("enter radius,side,length and breadth").split()]
print("area of circle a_c=%f \n perimeter of circle p_c=%f \n area of square a_s=%f \n perimeter of square p_s=%f \n area of rectangle a_r=%f \n perimeter of rectangle p_r=%f" %(area_perimeter(r,a,l,b)))


