#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 13:48:21 2020

@author: zuoxichen
"""

def get_array_numbers(integer):
    '''

    Parameters
    ----------
    int1 : integer
        int.

    Returns
    -------
    a set that contains all the number in a part.

    '''
    a=integer//3
    b=integer%3
    if b:
        list1=set(a,a+1)
    else:
        list1=set(a,a+1,a+b)
    return list1
num=0
n=int(input())
l1=list(int(i) for i in input().split())
set1=get_array_numbers(n)

    

