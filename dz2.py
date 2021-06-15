import math
from fractions import Fraction
import itertools

# part1
T = 0
Tt = 2000 
R = 1000
m = 259

def modInverse(a, m):
    for x in range(1, m, 1):
        if ((a % m) * (x % m)) % m == 1:
            return x

Rr = modInverse(R, m)
Mm = modInverse(-m, R)

for i in range(T, Tt, 1):
    U = (i * Mm) % R
    if ((i + U*m) / R) - ((i*Rr) % m) == m:
        if i != m:
            print("Part1: " + str(i))

# part2

def crt(primes, nums):
    prod = 1
    for p in primes:
        prod *= p
    result = 0
    for i in range(len(primes)):
        pp = prod // primes[i]
        result = result + nums[i] * modInverse(pp, primes[i]) * pp
    return result % prod


primes = [7, 11, 13]
nums = [4, 0, 8]

print("Part 2: " + str(crt(primes, nums)))

# part3

def f(d):
    print(d)
    sd = math.sqrt(d)
    i = 0
    a = []
    alpha = [sd]
    s = [0]
    t = [1]
    while True:
        a.append(int(alpha[i]))
        if (a[0] * 2 == a[i]):
            return a
        s.append(a[i] * t[i] - s[i])
        t.append((d - s[i + 1]**2) / t[i])
        alpha.append((s[i + 1] + sd) / t[i + 1])
        i += 1



i = 1
while True:
    if int(math.sqrt(i)) * int(math.sqrt(i)) == i:
        i += 1
        continue

    P = f(i)
    if len(P) == 26:
        print(i)
        print(P)
        break
    i += 1

