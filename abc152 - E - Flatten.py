# https://atcoder.jp/contests/abc152/tasks/abc152_e

import io

s = '''3
1000000 999999 999998
'''

f = io.StringIO(s)
N, *A = map(int, f.read().split())
mod = 10 ** 9 + 7


# 最小素因数を求める（エラトステネスの篩の亜種？）
def min_factor(n):
    sieve = list(range(n + 1))
    sieve[2::2] = [2] * (n // 2)
    for i in range(3, int(n ** 0.5) + 2, 2):
        if sieve[i] == i:
            sieve[i * i::2 * i] = [i] * ((n - i * i) // (2 * i) + 1)
    return sieve


# 素因数分解


def prime_factorize(n):
    a = {}
    while n != 1:
        b = table[n]
        if b in a:
            a[b] += 1
        else:
            a[b] = 1
        n //= b
    return a


table = min_factor(10 ** 6)

dic = {}
for i in A:
    for key, value in prime_factorize(i).items():
        if key in dic:
            dic[key] = max(dic[key], value)
        else:
            dic[key] = value

lcm = 1
for i, j in dic.items():
    lcm *= pow(i, j, mod)
    lcm %= mod

answer = sum(lcm * pow(i, mod - 2, mod) for i in A) % mod
print(answer)
