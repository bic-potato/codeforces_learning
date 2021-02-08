#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 16:09:47 2020

@author: zuoxichen
"""
def string_to_lists(string):
    list1=list()
    for i in string:
        list1.append(i)
    return list1

def CompareNext(number,list):
    n=0
    out=0
    while n<number-1:
        if(list[n]==list[n+1]):
            out+=1
            n+=1
            continue
        else:
            n+=1
    return out
a=int(input())
b=input()
list1=string_to_lists(b)
print(CompareNext(a,list1))
