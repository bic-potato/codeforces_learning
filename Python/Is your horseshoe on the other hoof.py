list1 = list(map(int, input().split()))
list2 = []
for i in list1:
    if i in list2:
        continue
    else:
        list2.append(i)
print(4 - len(list2))
