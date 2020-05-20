# https://atcoder.jp/contests/abc146/tasks/abc146_c

import io

a = '''1234 56789 314159265
'''
f = io.StringIO(a)
readline = f.readline

A, B, X = map(int, readline().split())
if (A * 10 ** 9 + B * 10) <= X:
    print(10 ** 9)
    quit()
if (A + B) > X:
    print(0)
    quit()


def find(X, rng):
    if len(rng) == 1:
        print(rng.start)
        return
    n = (rng.start + rng.stop) // 2
    cost = A * n + B * len(str(n))

    if cost < X:
        find(X, range(n, rng.stop))
    elif cost > X:
        find(X, range(rng.start, n))
    else:
        print(n)
        return


find(X, range(1, 1000000000))
