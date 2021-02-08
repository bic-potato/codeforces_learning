
list1=list(int(i) for i in input().split())
m=list1[0]
n=list1[1]
p=list1[2]
q=list1[3] 
i=0
j=0
array1=[]
array2=[]
arrayout=[]
while i<m:
    line=list(int(i) for i in input().split())
    array1.append(line)
    i+=1
while j<p:
    line=list(int(i) for i in input().split())
    array2.append(line)
    j+=1
for j in range(m-p+1):
    for i in range(n-q+1):
        trans=[]
        for k in range(p):
            for m in range(q):
                trans.append(array2[k][m]*array1[j+k][i+m])
        arrayout.append(sum(trans))
for i in range(len(arrayout)):
    if (i+1)%(n+1-q)!=0:
        print(arrayout[i],end=' ')
    else:
        print(arrayout[i])
