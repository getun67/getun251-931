import random

def vos(x):
    n = x
    l = [random.randint(2, 103) for i in range(n)]
    print(l)

    for i in range(n-1):
        il = i

        for j in range(i+1, n):
            if l[j] < l[il]:
                il = j

        l[i], l[il] = l[il], l[i]

    print(l)


def ub(x):
    n = x
    l = [random.randint(0, 100) for i in range(n)]
    print(l)

    for i in range(n-1):
        il = i

        for j in range(i+1, n):
            if l[j] > l[il]:
                il = j

        l[i], l[il] = l[il], l[i]

    print(l)


def nom():

    l = ["67-42-52", "12-03-52", "11-42-20", "17-17-18", "67-42-52"]
    n = len(l)


    for i in range(n-1):
        il = i

        for j in range(i+1, n):
            if l[j] < l[il]:
                il = j

        l[i], l[il] = l[il], l[i]

    print(l)


print(vos(10))
print(ub(10))
print(nom())
