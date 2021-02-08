n, m = map(int, input().split())
list1 = list(map(int, input().split()))
list1.sort()
list2 = []
for i in range(n-1):
    list2.append(list1[i+1]-list1[i])
list2.sort()
print(sum(list2[0:n-m]))


