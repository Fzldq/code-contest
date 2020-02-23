# https://atcoder.jp/contests/abc150/tasks/abc150_f

import io

a = '''5
0 0 0 0 0
2 2 2 2 2
'''
f = io.StringIO(a)

read = f.read
readline = f.readline
readlines = f.readlines

n, *lst = map(int, read().split())
al = lst[:n]
bl = lst[n:]


def convert(A):
    return [x ^ y for x, y in zip(A, A[1:])] + [A[-1] ^ A[0]]


a = convert(al)
b = convert(bl)


def Z_algorithm(s):
    n = len(s)
    z = [0] * n
    l, r = 0, 0
    for i in range(1, n):
        if i <= r:
            z[i] = z[i - l] if z[i - l] < r - i else r - i - 1
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1
    return z


Z = Z_algorithm(b + [-1] + a + a)[n + 1:n + n + 1]

K = [i for i, x in enumerate(Z) if x == n]
X = [al[k] ^ bl[0] for k in K]

print('\n'.join('{} {}'.format(k, x) for k, x in zip(K, X)))
