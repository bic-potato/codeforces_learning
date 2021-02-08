#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 15:05:59 2020

@author: zuoxichen
"""
def game_rule(i,j,arrayin,state_transfer):
    if state_transfer.count(1)<2 or state_transfer.count(1)>3:
        a=0
    elif arrayin[i][j]==0 and state_transfer.count(1)==3:
        a=1
    else:
        a=arrayin[i][j]
    return a
mn=list(int(i) for i in input().split())
n=mn[0]# n lines
m=mn[1]
i=0
arrayin=[]
while i<n:
    arrayin.append(list(int(i) for i in input().split()))
    i+=1
    arrayout=[]
for i in range(n):
    arrayout.append(list(i for i in range(m)))
    
for i in range(1,n-1):
    for j in range(1,m-1):
        state_transfer=[arrayin[i][j-1],arrayin[i][j+1],arrayin[i-1][j],arrayin[i+1][j],arrayin[i-1][j-1],arrayin[i-1][j+1],arrayin[i+1][j-1],arrayin[i+1][j+1]]
        arrayout[i][j]=game_rule(i,j,arrayin, state_transfer)
for j in range(1,m-1):
    state_transfer_up=[arrayin[0][j-1],arrayin[1][j-1],arrayin[1][j+1],arrayin[0][j+1],arrayin[1][j]]
    state_transfer_down=[arrayin[n-1][j-1],arrayin[n-2][j-1],arrayin[n-2][j+1],arrayin[n-1][j+1],arrayin[n-2][j]]
    arrayout[0][j]=game_rule(0,j,arrayin, state_transfer_up)
    arrayout[n-1][j]=game_rule(n-1, j, arrayin, state_transfer_down)
for i in range(1,n-1):
    state_transfer_up=[arrayin[i-1][0],arrayin[i+1][0],arrayin[i][1],arrayin[i-1][1],arrayin[i+1][1]]
    state_transfer_down=[arrayin[i-1][m-1],arrayin[i+1][m-1],arrayin[i][m-2],arrayin[i-1][m-2],arrayin[i+1][m-2]]
    arrayout[i][0]=game_rule(i,0,arrayin, state_transfer_up)
    arrayout[i][m-1]=game_rule(i, m-1, arrayin, state_transfer_down)
arrayout[0][0]=game_rule(0,0,arrayin,[arrayin[0][1],arrayin[1][1],arrayin[1][0]])
arrayout[0][m-1]=game_rule(0,m-1,arrayin,[arrayin[0][m-2],arrayin[1][m-1],arrayin[1][m-2]])
arrayout[n-1][0]=game_rule(n-1,0,arrayin,[arrayin[n-1][1],arrayin[n-2][1],arrayin[n-2][0]])
arrayout[n-1][m-1]=game_rule(n-1,m-1,arrayin,[arrayin[n-2][m-1],arrayin[n-1][m-2],arrayin[n-2][m-2]])
for i in range(n):
    for j in range(m):
        if j==m-1:
            print(arrayout[i][j])
        else:
            print(arrayout[i][j],end=' ')