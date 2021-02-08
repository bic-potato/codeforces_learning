def td_list ():
    n=0
    list1=list()
    while (n<5):
        a=input()
        list1.extend(a.split(' '))
        n+=1
    else:
        return(list1)
lit1=td_list()
a=lit1.index('1')
if (a==12):
    print('0')
else:
    if ((a==0)or(a==4)or(a==20)or(a==24)):
        print('4')
    else:
        if ((a==7)or(a==11)or(a==13)or(a==17)):
            print('1')
        else:
            if ((a==1)or(a==3)or(a==5)or(a==9)or(a==15)or(a==19)or(a==21)or(a==23)):
                print('3')
            else:
                print('2')
