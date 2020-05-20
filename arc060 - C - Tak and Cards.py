# https://atcoder.jp/contests/arc060/tasks/arc060_a

import io
from collections import defaultdict

s = '''8 5
3 6 2 8 7 6 5 9
'''

read = io.StringIO(s).read


def main():
    _, A, *xlst = map(int, read().split())
    x_p = []
    x_n = []
    x_z = 0
    for i in xlst:
        if A < i:
            x_p.append(i - A)
        elif i < A:
            x_n.append(A - i)
        else:
            x_z += 1
    x_p.sort(), x_n.sort()

    x_p_sum, x_n_sum = defaultdict(int, {0: 1}), defaultdict(int, {0: 1})

    for i in range(len(x_p)):
        for j in sorted(x_p_sum, reverse=1):
            x_p_sum[j + x_p[i]] += x_p_sum[j]

    for i in range(len(x_n)):
        for j in sorted(x_n_sum, reverse=1):
            x_n_sum[j + x_n[i]] += x_n_sum[j]

    res = sum(x_n_sum[i] * x_p_sum[i] for i in x_p_sum if i in x_n_sum)
    res *= 1 << x_z
    res -= 1
    print(res)


if __name__ == '__main__':
    main()
