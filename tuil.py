from math import sqrt, floor
from typing import List, Tuple


def gcd(a: int, b: int) -> int:
    a, b = max(a, b), min(a, b)
    while b > 0:
        a, b = b, a % b
    return a


def is_remainder(a: int, p: int) -> bool:
    # is x^2 === a (mod p)
    for x in range(1, p):
        if x**2 % p == a % p:
            return True
    return False


def get_all_semi_prime(n: int) -> int:
    for i in range(2, n):
        if gcd(n, i) == 1:
            yield i


def continued_fraction(a: int, b: int) -> List[int]:
    cf = []
    while b > 0:
        cf.append(a // b)
        a, b = b, a % b
    return cf


def get_convergent(cf: List[int]) -> List[Tuple[int, int]]:
    cvg = []
    p = [1, cf[0]]
    q = [0, 1]
    for i in range(1, len(cf)):
        cvg.append((p[i], q[i]))
        p.append(cf[i] * p[i] + p[i - 1])
        q.append(cf[i] * q[i] + q[i - 1])
    cvg.append((p[len(p) - 1], q[len(q) - 1]))
    return cvg


def prime(n: int) -> bool:
    if n == 2: return True
    if n == 1: return False
    for i in range(3, int(sqrt(n))):
        if n % i == 0:
            return False
    return True


def jacob_symbol(b: int, n: int) -> int:
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


def euler_pseudoprime(b: int, n: int) -> bool:
    return (jacob_symbol(b, n) % n) == pow(b, (n - 1) // 2, n)


def strong_pseudoprime(b: int, n: int) -> bool:
    if n % 4 == 3: return euler_pseudoprime(b, n)
    s, t = 0, n - 1
    while t % 2 == 0:
        t //= 2
        s += 1
    if pow(b, t, n) == 1: return True
    for r in range(1, s):
        if pow(b, (2**r) * t, n) == -1: return True
    return False


def pollards_roh_method(n: int) -> int:
    f = lambda x: (x**2 - 1) % n
    for slow in [2, 3, 4, 6]:
        steps, i, fast = 2 * floor(sqrt(sqrt(n))), 0, slow
        while i < steps:
            slow = f(slow)
            fast = f(f(fast))
            p = gcd(fast - slow, n)
            if p != 1:
                if p == n: break
                else: return p
    return 1
