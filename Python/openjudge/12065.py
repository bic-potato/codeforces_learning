i = 0
m = 50
n = -50
while i<100000:
    b = (m + n)/2
    if b **3 - 5 * b **2 + 10 * b -80 >0:
        m = b
    else:
        n = b
    i += 1
c = (m + n)/2
print("%.9f"%c)