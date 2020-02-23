# https://atcoder.jp/contests/abc154/tasks/abc154_f

import numpy as np
import io

s = '314 159 2653 589'
f = io.StringIO(s)
read = f.read
r1, c1, r2, c2 = map(int, read().split())
MOD = 10 ** 9 + 7


def cumprod(A, MOD=MOD):
    L = len(A)
    Lsq = int(L**.5 + 1)
    A = np.resize(A, Lsq**2).reshape(Lsq, Lsq)
    for n in range(1, Lsq):
        A[:, n] *= A[:, n - 1]
        A[:, n] %= MOD
    for n in range(1, Lsq):
        A[n] *= A[n - 1, -1]
        A[n] %= MOD
    return A.ravel()[:L]


def make_fact(U, MOD=MOD):
    x = np.arange(U, dtype=np.int64)
    x[0] = 1
    fact = cumprod(x, MOD)
    x = np.arange(U, 0, -1, dtype=np.int64)
    x[0] = pow(int(fact[-1]), MOD - 2, MOD)
    fact_inv = cumprod(x, MOD)[::-1]
    fact.flags.writeable = False
    fact_inv.flags.writeable = False
    return fact, fact_inv


fac, finv = make_fact(2 * 10**6 + 10, MOD)


def comb(n, k):
    if n < k:
        return 0
    if n < 0 or k < 0:
        return 0
    return fac[n] * (finv[k] * finv[n - k] % MOD) % MOD


answer = comb(r2 + c2 + 2, r2 + 1) - comb(c1 + r2 + 1, c1) - \
    comb(r1 + c2 + 1, r1) + comb(r1 + c1, r1)
answer %= MOD
print(answer)
