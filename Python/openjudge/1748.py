class King:
    def __init__(self,n):
        self.round=list(range(1,n+1))
    def chooseKing(self,m):
        j = 0
        i = 1
        n = 0
        length = len(self.round)
        while n < length-1:
            if j == length-1:
                j = 0
            else:
                j += 1
            if self.round[j] != 0 and i != m:
                i += 1
            elif i + 1 == m :
                i = 1
                self.round[j] = 0
                n += 1
        return self.printKing
    @property
    def printKing(self):
        set1 = set(self.round)
        for i in set1:
            if i != 0:
                print(i)
                break

judge = True
while judge :
    n,m = map(int,input().split())
    if n == 0 and m == 0:
        break
    else:
        king = King(n)
        king.chooseKing(m)  
