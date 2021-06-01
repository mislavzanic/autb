from math import sqrt


def isRemainder(a: int, p: int) -> bool:
    # is x^2 === a (mod p)
    for x in range(1, p):
        if x**2 % p == a % p:
            return True
    return False


def zad1(p: int) -> int:
    for a in range(1, p):
        if not isRemainder(a, p):
            return a


def zad2(p: int, b: int) -> int:
    for x in range(1, p):
        if x**2 % p == b % p:
            yield x


def zad3():
    a, b = sqrt(2), sqrt(73)
    q, p1, p2 = 1189751, 1682562, 10165237
    return min(abs(a - p1 / q), abs(b - p2 / q)) < q ** (-1.5)


def main():
    p, b = 2441, 2237
    print(zad1(p))
    print(zad2(p, b))
    print(zad3())


if __name__ == '__main__':
    main()
