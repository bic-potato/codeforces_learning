def split_into_ascii ():
    string=input()
    list1=string.split("+")
    list2=list()
    for i in list1:
        a=ord(i)
        list2.append(a)
    return(list2)
def reverse_ascii(list1):
    list2=list()
    for j in list1:
        a=chr(int(j))
        list2.extend(a)
    return(list2)
list1=split_into_ascii()
list1.sort()
list2=reverse_ascii(list1)
str1=str("+").join(list2)
print(str1)