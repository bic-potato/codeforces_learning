class Vector:
    @property
    def dot_product(self,vector):
        vecout = []
        for i in range(self.dim):
            vecout.append(vector.vecdata[i]*self.vecdata[i])
        vecout = sum(vecout)
    
    def __init__(self,list1):
        self.vecdata = list1
        self.dim = len(list1)

n = int(input())
if n % 2 != 0:
    print('1')
else:
    print(n)