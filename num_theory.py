from math import sqrt, floor
from typing import List, Tuple, Any, Callable
from functools import reduce
from collections import defaultdict
import itertools


def gcd(a: int, b: int) -> int:
    a, b = max(a, b), min(a, b)
    while b > 0:
        a, b = b, a % b
    return a


def lcm(l: List[int]) -> int:
    return reduce(lambda x, y: x * y // gcd(x, y), l)


def is_remainder(a: int, p: int) -> bool:
    # is x^2 === a (mod p)
    for x in range(1, p):
        if x ** 2 % p == a % p:
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


def continued_fraction_i(d) -> Tuple[List[int], List[int], List[int]]:
    sqrt_d = sqrt(d)
    a, s, t, alpha = [], [0], [1], [sqrt_d]
    i = 0
    while True:
        a.append(int(alpha[i]))
        if (a[0] * 2 == a[i]):
            return a, s, t
        s.append(a[i] * t[i] - s[i])
        t.append((d - s[i + 1]**2) // t[i])
        alpha.append(((s[i + 1] + sqrt_d) / t[i + 1]))
        i += 1


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
    for i in range(3, int(sqrt(n) + 1)):
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


def pseudoprime(b: int, n: int) -> bool:
    if not prime(n) and gcd(b, n) == 1:
        if pow(b, n - 1, n) == 1: return True
    return False


def euler_pseudoprime(b: int, n: int) -> bool:
    return (jacob_symbol(b, n) % n) == pow(b, (n - 1) // 2, n)


def strong_pseudoprime(b: int, n: int) -> bool:
    if n % 4 == 3:
        print(str(n) + ' % 4 == 3')
        return euler_pseudoprime(b, n)
    s, t = 0, n - 1
    while t % 2 == 0:
        t //= 2
        s += 1
    print('s: ' + str(s) + ', t: ' +  str(t))
    if pow(b, t, n) == 1:
        print('(' + str(b) + ' ^ ' + str(t) + ') % ' + str(n) + ' == 1 -- b ^ t % n == 1')
        return True
    for r in range(1, s+1):
        print('b ^ ((2 ^ r) * t) % n = ' + str(pow(b, (2 ** r) * t, n)))
        if pow(b, (2 ** r) * t, n) == -1: return True
    return False


def pollards_roh_method(n: int, x0: int, f: Callable[[int], int]) -> int:
    for slow in [x0]:
        steps, i, fast = 2 * floor(sqrt(sqrt(n))), 0, slow
        while i < steps:
            slow = f(slow) % n
            fast = f(f(fast) % n) % n
            p = gcd(abs(fast - slow), n)
            print('x_' + str(i + 1) + ' = ' + str(slow))
            print('y_' + str(i + 1) + ' = ' + str(fast))
            print('nzd('+ str(abs(fast - slow)) + ', ' + str(n) + ') = ' + str(p))
            i += 1
            if p != 1:
                if p == n: break
                else: return p
    return 1


def pollards_pm1_method(n: int, B: int, a: int) -> int:
    m = lcm(list(range(2, B + 1)))
    factor = pow(a, m, n)
    print('m: ' + str(m) + ', a ^ m % n == ' + str(factor))
    p = gcd(factor - 1, n)
    return p


def is_complete_square(prod):
    divisors = defaultdict(int)
    factor = 2
    while prod > 1:
        while prod % factor == 0:
            divisors[factor] += 1
            prod //= factor
        factor += 1
    for k, v in divisors.items():
        if v % 2 != 0:
            return False
    return True



def continued_fract_method(n: int) -> int:
    a, s, t = continued_fraction_i(n)
    i = 0
    p = []
    seen = {1, n}
    while i < len(a):
        if i == 0: p.append(a[i])
        elif i == 1: p.append(a[i] * p[i - 1] + 1 % n)
        else: p.append((a[i] * p[i - 1] + p[i - 2]) % n)
        t[i] = t[i] * (-1)**i
        i += 1
    t = t[:len(t) // 2]
    for size in range(1, len(t)):
        subset = itertools.combinations(t, size)
        for item in subset:
            prod = reduce(lambda x, y: x * y, item)
            if prod > 0 and is_complete_square(prod) and prod != 1:
                pp, pp2 = 1, 1
                for num in item:
                    pp *= p[t.index(num) - 1]
                    pp2 *= p[t.index(num) - 1] ** 2
                if pp2 % n == prod % n:
                    temp = gcd(pp % n + int(sqrt(prod)) % n, n)
                    if n % temp == 0 and temp not in seen:
                        print(item, t)
                        seen.add(temp)
                        yield gcd(pp % n + int(sqrt(prod)), n)


if __name__ == '__main__':
    print('Jak pseudoprosti broj: ')
    print(strong_pseudoprime(b=4, n=1105))
    print('Pollardova ro metoda: ')
    print(pollards_roh_method(n=2449, x0=2, f=lambda x: x**2 - 1))
    print('Pollardova p - 1 metoda')
    print(pollards_pm1_method(n=633211, B=8, a=2))
    print('Cont fract meth')
    for i in continued_fract_method(25511):
        print(i)
