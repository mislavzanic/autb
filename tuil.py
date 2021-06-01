from math import sqrt


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def get_all_semi_prime(n):
    for i in range(2, n):
        if gcd(n, i) == 1:
            yield i


def calculate(a, m, n):
    if m == 1:
        return a % n
    elif m % 2 == 0:
        return calculate((a ** 2) % n, m / 2, n) % n
    else:
        return (a * calculate(a % n, m - 1, n)) % n


def continued_fraction(a, b):
    cf = []
    while b > 0:
        cf.append(a // b)
        a, b = b, a % b
    return cf


def get_convergent(cf):
    cvg = []
    p = [1, cf[0]]
    q = [0, 1]
    for i in range(1, len(cf)):
        cvg.append((p[i], q[i]))
        p.append(cf[i] * p[i] + p[i - 1])
        q.append(cf[i] * q[i] + q[i - 1])
    cvg.append((p[len(p) - 1], q[len(q) - 1]))
    return cvg


def prime(n):
    if n == 2: return True
    if n == 1: return False
    for i in range(3, int(sqrt(n))):
        if n % i == 0:
            return False
    return True


def jacob_symbol(b, n):
    b, t = b % n, 1
    while b != 0:
        while b % 2 == 0:
            b = b // 2
            if n % 8 in {3, 5}: t = -t
        b, n = n, b
        if b % 4 == n % 4 == 3: t = -t
        b %= n
    if n == 1: return t
    return 0


def euler_pseudoprime(b, n):
    return (jacob_symbol(b, n) % n) == (calculate(b, (n - 1) // 2, n) % n)
