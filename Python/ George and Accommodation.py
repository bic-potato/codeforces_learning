n=int(input())
i=0
j=0
while i<n:
	str1=input()
	b=str1.split(' ')
	if (int(b[1])-int(b[0])>=2):
		j+=1
	i+=1
print(j)
		
