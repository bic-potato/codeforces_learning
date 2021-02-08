direction = [[-1,0], [0, -1], [0, 1], [1, 0]]
n, m = map(int, input().split())
matix = [[0]* (m + 2)]
length = 0
for _ in range(n):
    list1 = [0]
    list1.extend(list(map(int, input().split())))
    list1.append(0)
    matix.append(list1)
matix.append([0] * (m + 2))
for i in range(1,n+1):
    for j in range(1,m+1):
        if matix[i][j] == 1:
            for k in direction:
                if matix[i + k[0]][j + k[1]] == 0:
                    length += 1
print(length)