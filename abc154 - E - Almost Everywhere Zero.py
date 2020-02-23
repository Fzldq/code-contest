# https://atcoder.jp/contests/abc154/tasks/abc154_e

import io

s = '''9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
3
'''
f = io.StringIO(s)
read = f.read

n, k = map(int, read().split())


def count(digit, k):
    if digit < k:
        return 0
    elif k == 0:
        return 1
    elif k == 1:
        return digit
    elif k == 2:
        return digit * (digit - 1) // 2
    else:
        return digit * (digit - 1) * (digit - 2) // 6


def solve(n, k):
    if k == 0:
        return 1
    digit = len(str(n))
    res = 0
    if digit > k:
        res += count(digit - 1, k) * (9 ** k)
    pow10 = 10 ** (digit - 1)
    d, mod = n // pow10, n % pow10
    res += count(digit - 1, k - 1) * (9 ** (k - 1)) * (d - 1)
    res += solve(mod, k - 1)
    return res


print(solve(n, k))
