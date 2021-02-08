for _ in range(int(input())):
    list1 =[]
    i, j, k, m = map(int, input().split())
    for a in [i, -i]:
        for b in [j, -j]:
            for c in [k, -k]:
                for d in [m, -m]:
                    list1.append(a + b + c + d)
    if 24 in list1:
        print('YES')
    else:
        print("NO")