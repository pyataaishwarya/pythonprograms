#!/bin/python

def percentage(s1,s2,s3,s4,s5,s6,tot):
    per=((s1+s2+s3+s4+s5+s6)/tot)*100
    return per
s1,s2,s3,s4,s5,s6,tot=[eval(x) for x in input("enter the marks in s1,s2,s3,s4,s5,s6 and tot").split()]
p=percentage(s1,s2,s3,s4,s5,s6,tot)
if p>80:
    print("honours")
elif p>=60 and p<80:
    print("first division")
elif p>=50 and p<60:
    print("second division")
elif p>=40 and p<50:
    print("third division")
else:
    print("fail")


