a=input()
b=input()
list1=a.split(' ')
list2=b.split(' ')
n=int(list1[0])
k=int(list1[1])
i=0
n1=n
while i<n:
	c=int(list2[i])
	if c>k:
		n1+=1
	i+=1
else:
	print(n1)
