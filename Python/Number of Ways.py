def get_arrays(inteage):
    if inteage % 3 == 0:
        a = set(inteage/3)
    elif inteage % 3 == 1:
        a = set(inteage//3, inteage//3+1)
    else:
        a = [set(inteage//3, inteage // 3 + 1, inteage//3 + 2)]
    return a
def mod2_arg (set1):
    a = 0
    print(set())