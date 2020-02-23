import numpy as np
mod = 10 ** 9 + 7


def cumprod(A, mod=mod):
    L = len(A)
    Lsq = int(L**.5 + 1)
    A = np.resize(A, Lsq**2).reshape(Lsq, Lsq)
    for n in range(1, Lsq):
        A[:, n] *= A[:, n - 1]
        A[:, n] %= mod
    for n in range(1, Lsq):
        A[n] *= A[n - 1, -1]
        A[n] %= mod
    return A.ravel()[:L]


def make_fact(U, mod=mod):
    x = np.arange(U, dtype=np.int64)
    x[0] = 1
    fact = cumprod(x, mod)
    x = np.arange(U, 0, -1, dtype=np.int64)
    x[0] = pow(int(fact[-1]), mod - 2, mod)
    fact_inv = cumprod(x, mod)[::-1]
    fact.flags.writeable = False
    fact_inv.flags.writeable = False
    return fact, fact_inv


def comb(n, k, mod=mod):
    if n < k:
        return 0
    if n < 0 or k < 0:
        return 0
    return fac[n] * (finv[k] * finv[n - k] % mod) % mod


fac, finv = make_fact(2 * 10**6 + 10, mod)
print(comb(10, 3))
