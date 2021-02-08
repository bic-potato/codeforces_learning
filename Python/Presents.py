def print_dic(n,dic1):
	i=0
	while i<n:
		print(dic1[i+1],end=" ")
		i+=1

def create_dict(n):
	list1=(range(1,n))
	tup1=tuple(list1)
	dict1=dict.fromkeys(tup1)
	return dict1
	
def main_args():
	n=int(input())
	a=input()
	list1=a.split(' ')
	dict1=create_dict(n)
	i=1
	while i<=n:
		j=int(list1[i-1])
		dict1[j]=i
		i+=1
	else:
		print_dic(n,dict1)
		
main_args()
