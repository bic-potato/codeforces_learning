#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 17:31:03 2020

@author: zuoxichen
"""
def String_to_Lists(String):
    list1=list(String.split(' '))
    return list1
def main_approach (list):
    k=int(list[0])
    n=int(list[1])
    w=int(list[2])
    i=0
    sums=0
    while i<w:
        i+=1
        a=i*k
        sums=sums+a
    if (sums-n)<0:
        print('0')
    else:
        print(sums-n)
str1=input()
list1=String_to_Lists(str1)
main_approach(list1)