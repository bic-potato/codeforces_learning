#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 13:12:45 2020

@author: zuoxichen
"""

n=int(input()) # get number
i=0 # create a timer
list1=[] # create an empty list
while i<n:
    if i%2==0:
        list1.append('I hate')   # while i is even; add 'I hate'
    else:
   		list1.append('I love')   # while i is odd; add 'I love'
    if i<n-1:
    	list1.append('that')     # add connection word 'that'
    else:
   		list1.append('it')       # while the loop is end, add 'it'
    i+=1
for i in list1:
   	print(i,end=' ')             # print as a string