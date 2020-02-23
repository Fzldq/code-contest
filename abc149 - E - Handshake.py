# https://atcoder.jp/contests/abc149/tasks/abc149_e

import numpy as np
import io

a = '''9 73
67597 52981 5828 66249 75177 64141 40773 79105 16076
'''
f = io.StringIO(a)

N, M = map(int, f.readline().split())
A = np.array(f.read().split(), np.int64)

A.sort()


def shake_cnt(x):
    # x 以上の握手を全て行うとして、握手の回数を数える
    # 行わない握手を数える
    X = np.searchsorted(A, x - A)
    return N * N - X.sum()


left = 0  # 握手の回数がM以上
right = 10 ** 6  # 握手の回数がM未満
while left + 1 < right:
    x = (left + right) // 2
    if shake_cnt(x) >= M:
        left = x
    else:
        right = x

left, right

# right 以上の握手を全て行ったとして、回数と総和を計算

X = np.searchsorted(A, right - A)  # 行わない人数
Acum = np.zeros(N + 1, np.int64)  # 人数 -> 累積和
Acum[1:] = np.cumsum(A)

shake = N * N - X.sum()
happy = (Acum[-1] - Acum[X]).sum() + \
        (A * (N - X)).sum()

happy += (M - shake) * left
print(happy)
