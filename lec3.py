def zad1(n, k=1):
    if k > n:
        return
    print(k)
    zad1(n, k + 1)


def zad2(a,b):
    if a < b:
        zad2_1(a, b)
    else:
        zad2_2(a, b)


def zad2_1(a, b):
    if a > b:
        return
    print(a)
    zad2_1(a + 1, b)


def zad2_2(a, b):
    if a < b:
        return
    print(a)
    zad2_2(a-1, b)


def zad3(n):
    if n == 0:
        return 0

    return (n % 10) + zad3(n // 10)


def zad4_a(c, d):
    if c % d == 0:
        return zad4_a(c // d, d)
    return c


def zad4(n, dell = 2):
    if dell * dell > n:
        print(n)
        return
    if n % dell == 0:
        print(dell)
        n = zad4_a(n, dell)
    zad4(n, dell + 1)



#zad1(7)
#zad2(3, 12)
#print(zad3(769))
zad4(12)
