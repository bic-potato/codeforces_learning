n=int(input())
str1=input()
a=0
for i in str1:
	if i=='A':
		a+=1
if n/2<a:
	print('Anton')
elif n/2>a:
	print('Danik')
else:
	print('Friendship')
