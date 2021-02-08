#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 20:49:48 2020

@author: zuoxichen
"""

def count_numbers(strings):
    l=0
    n=0
    for i in strings:
        if i.islower():
            l+=1
        else:
            l+=0
        n+=1
    list1=[n,l]
    return(list1)
    
def main_args():
    a=input()
    b=count_numbers(a)
    if (b[0]/2)>b[1]:
        print(a.upper())
    else:
        print(a.lower())
        
main_args()