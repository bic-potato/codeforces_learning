def split_into_ascii (string):
    list1=list()
    for i in string:
        a=ord(i)
        list1.append(a)
    return(list1)
def compare (string1,string2):
    for i,j in zip(string1,string2):
        k=int(i)
        l=int(j)
        if(k==l):
            continue
        else:
            if(k<l):
                print('-1')
                break
            else:
                print('1')
                break
string1=input()
string2=input()
s1=str(string1.lower())
s2=str(string2.lower())
a=split_into_ascii(s1)
b=split_into_ascii(s2)
if (a==b):
    print("0")
else:
    compare(a,b)