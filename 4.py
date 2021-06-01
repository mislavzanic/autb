from tuil import *


def zad1():
    n, e, d = 9827933, 17, 3177473
    m = (e * d - 1) / 2
    candidates = [a for a in get_all_semi_prime(n)]
    k = 1
    while m % 2 == 0:
        for a in candidates:
            b = pow(a, m, n)
            if b != 1:
                return a, k, b  # 7, 2, nes

        m = m / 2
        k += 1


def zad2():
    n, e = 17641807, 9280619
    cvg = get_convergent(continued_fraction(e, n))
    x = 2
    for i in range(1, len(cvg)):
        xx = pow(x, e * cvg[i][1], n)
        if xx == x % n:
            return cvg[i][1]  # d = 19


def zad3():
    b = 48
    n = 3
    while True:
        if not prime(n) and gcd(max(b, n), min(b, n)) == 1:
            if pow(b, n - 1, n) == 1 and not euler_pseudoprime(b, n):
                return n  # 91

        n += 2


def main():
    print(zad1(), zad2(), zad3())


if __name__ == '__main__':
    main()
