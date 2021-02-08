#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 16:29:50 2020

@author: zuoxichen
"""
def FirstLetterUpper (string):
    a=string[0]
    b=string[1:-1]
    e=string[-1]
    f=int(len(string))
    c=a.capitalize()
    if (f==1):
        d=c+b
    else:
        d=c+b+e
    return d
str1=input()
output=FirstLetterUpper(str1)
print(output)