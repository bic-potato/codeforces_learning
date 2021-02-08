inputstr= list(input().lower())
listout = [[inputstr[0],1]]
for i in range(1, len(inputstr)):
    if inputstr[i-1] == inputstr[i]:
        listout[-1][1] += 1
    else:
        listout.append([inputstr[i], 1])
for i in listout:
    print("(%s,%d)"%(i[0], i[1]), end="")
