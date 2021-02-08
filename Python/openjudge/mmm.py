list0=list(map(int,input().split()))
n=list0[0]
m=list0[1]
list1=list(map(int,input().split()))
j=0
while i<m:
    cou=0
    list2=[]
    l=int(input())
    for i in range(l-1,n):
        if list1[i] in list2:
            continue
        else:
            cou+=1
            list2.append(list1[i])
    print(cou)
    j+=1
