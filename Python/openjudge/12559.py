#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 15:54:02 2020

@author: zuoxichen
"""

def bigger(str1, str2):
    if len(str1) > len(str2):
        for i in range(len(str2)):
            if int(str1[i]) > int(str2[i]):
                return True
            else:
                return False
        else:
            return True
    elif len(str1) < len(str2):
            for i in range(len(str1)):
                if int(str1[i]) > int(str2[i]):
                    return True
                elif int(str1[i]) == int(i
n = int(input())
list1 = input().split()
list1.sort(reverse=True)
maxstr=''
morestr=''
for i in range(len(list1)-1):
    if list1[i][0] != list1[i+1][0]:
        maxstr +=  morestr
        morestr = ''
        maxstr += list1[i]
    else:
        if not bigger(list1[i], list1[i+1]):
            middle = list1[i+1] + list1[i]
        else:
            middle = list1[i] + list1[i+1]
        if not bigger(morestr, middle):
            morestr = morestr + middle
        else:
            morestr = middle +morestr


maxstr += list1[-1]
list1.sort()
minstr = ''
lessstr = ''
for i in range(len(list1)-1):
    if list1[i][0] != list1[i+1][0]:
        minstr += lessstr
        lessstr = ''
        minstr += list1[i]
    else:
        if not bigger(list1[i], list1[i+1]):
            middle = list1[i] + list1[i+1]
        else:
            middle = list1[i+1] + list1[i]
        if not bigger(lessstr, middle):
            lessstr = lessstr + middle
        else:
            lessstr = middle +lessstr


minstr += list1[-1]
print(maxstr, end=' ')
print(minstr)