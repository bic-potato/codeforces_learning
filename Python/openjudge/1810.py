L,M = map(int,input().split())
allTrees=L+1
cou = 0
first = []
last = []
for _ in range(M):
    cache=list(map(int,input().split()))
    first.append(cache[0])
    last.append(cache[1])
else:
    dic1 = dict(zip(first,last))
    first.sort()
    count=[first[0],0]
    sums=0
    for i in range(len(first)-1):
        if dic1[first[i]] > first[i+1]:
            count[1] = dic1[first[i+1]] if dic1[first[i+1]] > dic1[first[i]] else dic1[first[i]]
        else:
            sums += count[1]-count[0] + 1
            count = [first[i+1]]
            if i == len(first)-2:
                sums+=dic1[first[i+1]] - first[i+1] + 1
    print(allTrees-sums)
