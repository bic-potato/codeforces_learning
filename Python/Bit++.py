n=int(input())
i=0
x=0
while (i<n):
    b=set(input())
    if("+" in b):
        x+=1
    else:
        x+=(-1)
    i+=1
else:
    print(x)
