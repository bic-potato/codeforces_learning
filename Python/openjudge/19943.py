#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 15:28:20 2020

@author: zuoxichen
"""
def creat_array(n):
    i=0
    D=[]
    while i<n:
        D.append([0]*n)
        i+=1
    return(D)
list1=list(int(i) for i in input().split())
n=list1[0]
m=list1[1]
k=0
D=creat_array(n)
A=creat_array(n)
L=creat_array(n)
while k<m:
    list2=list(int(i) for i in input().split())
    x=list2[0]
    y=list2[1]
    D[x][x]+=1
    D[y][y]+=1
    A[x][y]+=1
    A[y][x]+=1
    k+=1
else:
    for l in range(n):
        for q in range(n):
            L[l][q]=D[l][q]-A[l][q]

for i in range(len(L)):      
        for j in range(len(L[i])):    
            print(L[i][j], end=' ')
        print()