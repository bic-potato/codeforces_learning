#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 18:24:55 2020

@author: zuoxichen
"""

class Queen:
    chessboard = []
    Coor=[]
    def __init__(self):
        k=0
        while k < 8:
            Queen.chessboard.append([0]*8)
            k+=1
        self.search(0)
    def judgeBans(self,m,k):
        for i in range(len(Queen.Coor)):
            if (abs(k-i) == abs(m-self.Coor[i]) or m == self.Coor[i] or k == i):
                return False
        return True
    def addQueens(self,j):
        Queen.Coor.append(j)
    def search(self, k):
        if k == 8 :
            self.putChess
        else:
            for m in range(8):
                if self.judgeBans(m,k):
                    self.addQueens(m)
                    self.search(k+1)
    @property                
    def putChess(self):
        for i in range(len(Queen.Coor)):
            Queen.chessboard[i][self.Coor[i]] = 1
        for i in queen.chessboard:
            for j in i:
                print(j,end=' ')
            print()
        print(" ")



queen = Queen


                
