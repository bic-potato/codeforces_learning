#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 22:04:33 2020

@author: zuoxichen
"""
import sys
n=int(input())
a=input()
list1=a.split(" ")
for i in list1:
    if i=='1':
        print('HARD')
        sys.exit(0)
print('EASY')