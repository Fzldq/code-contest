# https://atcoder.jp/contests/arc067/tasks/arc067_a

from collections import defaultdict


def min_factor(n):
    sieve = list(range(n + 1))
    sieve[2::2] = [2] * (n // 2)
    for i in range(3, int(n ** 0.5) + 2, 2):
        if sieve[i] == i:
            sieve[i * i::2 * i] = [i] * ((n - i * i) // (2 * i) + 1)
    return sieve


def prime_factorize(n, table):
    a = {}
    while n != 1:
        b = table[n]
        if b in a:
            a[b] += 1
        else:
            a[b] = 1
        n //= b
    return a


def main():
    n = int(input())
    mod = 10 ** 9 + 7
    table = min_factor(10 ** 3)

    dic = defaultdict(int)
    for i in range(1, n + 1):
        for key, value in prime_factorize(i, table).items():
            dic[key] += value

    res = 1
    for value in dic.values():
        res *= value + 1
        res %= mod
    print(res)


if __name__ == '__main__':
    main()
