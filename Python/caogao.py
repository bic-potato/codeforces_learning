def split_into_ascii ():
    string=input()
    list1=string.split("+")
    list2=list()
    for i in list1:
        a=ord(i)
        list2.append(a)
    return(list2)
list1=split_into_ascii()
list2=list1.sort()
print(list1)
print(list2)