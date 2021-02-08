i = True
while i :
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    n, k = list(map(int, input().split()))
    if n == 0 and k == 0:
        break
    for _ in range(2):
        list1.append(list(map(int, input().split())))
    else:
        for i in range(n):
            list2.append(list1[0][i]/list1[1][i])
        list2.sort()
        for i in range(n):
            if list1[0][i]/list1[1][i] in list2[0 : k]:
                continue
            else:
                list3.append(list1[0][i])
                list4.append(list1[1][i])
        else:
            print(int(100 * (sum(list3) / sum(list4))))