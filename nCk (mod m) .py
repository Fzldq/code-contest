MOD = 10 ** 9 + 7
# pypyで通す


def prepare(n, MOD):

    # 1! - n! の計算
    f = 1
    factorials = [1]  # 0!の分
    for m in range(1, n + 1):
        f *= m
        f %= MOD
        factorials.append(f)
    # n!^-1 の計算
    inv = pow(f, MOD - 2, MOD)
    # n!^-1 - 1!^-1 の計算
    invs = [1] * (n + 1)
    invs[n] = inv
    for m in range(n, 1, -1):
        inv *= m
        inv %= MOD
        invs[m - 1] = inv

    return factorials, invs


def comb(n, k, mod, fac, finv):
    '''
    二項係数の計算

    Parameters
    n : int
        元集合
    k : int
        元集合から選択する数
    mod : int
        あまり
    fac : list
        階乗のリスト
    finv : list
        逆元のリスト

    Returns
    c : int
        nCkの組み合わせの数
    '''
    if n < k:
        return 0
    if n < 0 or k < 0:
        return 0
    return fac[n] * (finv[k] * finv[n - k] % mod) % mod


N = int(input())

fac, rfac = prepare(N, MOD)
# print(count)
# 最大値の数え上げ
maxnum = 0
minnum = 0
for i in range(N):
    counter = comb(N, i, MOD, fac, rfac)
    print(counter)
