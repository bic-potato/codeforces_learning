class Distance:
    distances = []
    def distance(self,pairs):
        str1 = ''
        int1 = 0
        for i in pairs:
            if i =='(' :
                continue
            elif i == ')':
                self.distances.append(int1 + int(str1))
                str1 = ''
                int1 = 0
            elif i ==',':
                int1 = int(str1)
                str1 = ''
            else:
                str1 += i
    def __init__(self,list1):
        for i in list1:
            self.distance(i)

class Middle:
    def middlenum(self, list1):
        list1.sort()    
        if self.n % 2 == 0:
            self.middle = (list1[int(self.n / 2) -1] + list1[int(self.n / 2)]) / 2
        elif n != 1:
            self.middle = list1[self.n // 2]
        else:
            self.middle = list1[0]

    def __init__(self, list1):
        self.n = len(list1)
        self.middlenum(list1)

n = int(input())
distancein = Distance(input().split())
money = list(map(int, input().split()))
compare = []
compare1 = []
money1 =[]
for i in range(len(money)):
    compare.append(distancein.distances[i]/money[i])
    compare1.append(compare[i])
    money1.append(money[i])
moneymiddle = Middle(money)
comparemiddle = Middle(compare)
con = 0
for i in range(n):
    if compare1[i] > comparemiddle.middle and money1[i] < moneymiddle.middle:
        con += 1
print(con)