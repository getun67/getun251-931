import random
import string


l = [random.randint(50, 100) for i in range(20)]
#print(l)

def zad1and2(l):
    if len(l) <= 1:
        return l

    x = l[0]
    lt = [i for i in l if i < x]
    rt = [i for i in l if i > x]
    return zad1and2(lt) + [x] + zad1and2(rt)

#print(zad1and2(l))

###################################################################

l1 = [[random.randint(5, 61) for j in range(4)] for i in range(5)]
#print(l1)

def zad3(l1):
    if len(l1) <= 1:
        return l1

    x = l1[0][0]

    lt = [i for i in l1 if i[0] < x]
    rt = [i for i in l1 if i[0] > x]

    return zad3(lt) + [l1[0]] + zad3(rt)
print()
#print(zad3(l1))

################################################################

zad4 = [''.join(random.choices(string.ascii_lowercase, k=5)) for i in range(6)]

zad4.sort()

print(zad4)
