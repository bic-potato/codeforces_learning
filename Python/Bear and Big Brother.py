#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 22:06:06 2020

@author: zuoxichen
"""
def String_to_list (Strings):
    list1=list(Strings.split(" "))
    return list1
def main_approach (num1,num2):
    i=0
    a=num1
    b=num2
    while a<=b :
        i+=1
        a=a*3
        b=b*2
    else:
        return i
input1=input()
list2=String_to_list(input1)
num1=int(list2[0])
num2=int(list2[1])
print(main_approach(num1, num2))
        
    

