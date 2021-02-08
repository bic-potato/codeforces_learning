<<<<<<< HEAD
import os
a=input()
b=input()
list1=list(a.split(" "))
list2=list(b.split(" "))
n=int(list1[0])
k=int(list1[1])
r=int(list2[0])
i=0
if(r==0):
    print(i)
    os._exit
else:
    if(n==k):
        print(k)
    else:
        while(i<k):
            i+=1
        else:
            p=list2[i-1]
            q=list2[i]
            if(p==0):
                os._exit
            else:
                while(p==q):
                    if(i<=n-2):
                        i+=1
                        q=list2[i]
                    else:
                        i=n
                        break
                else:
                    os._exit
        print(i)
=======
a=input()
b=input()
list1=list(a.split(" "))
list2=list(b.split(" "))
n=int(list1[0])
k=int(list1[1])
if '0' in list2:
    m=list2.index('0')
    if m<k:
        print(m)
    else:
        mini=list2[k-1]
        list3=list2[k-1:]
        q=list3.count(mini)
        if q==1:
            print(k)
        else:
            print(k+q-1)
else:
    mini=list2[k-1]
    list3=list2[k-1:]
    q=list3.count(mini)
    if q==1:
        print(k)
    else:
        print(k+q-1)
>>>>>>> 46c1d5c8dc6a415160913bd7cb25ceb44baac0a4
