import sys
a=input()
b=input()
c=list(a)
d=list(b)
d.reverse()
i=0
if len(c)!=len(d) :
	print('NO')
else:
	while i<len(a):
		if c[i]==d[i]:
			i+=1
			continue
		else:
			print('NO')
			break
			sys.exit(0)
	else:
		print('YES')
