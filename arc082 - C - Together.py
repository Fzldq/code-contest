# https://atcoder.jp/contests/arc082/tasks/arc082_a

import io
from itertools import accumulate

s = '''1
99999
'''


def main():
    read = io.StringIO(s).read
    n, *A = map(int, read().split())
    minA = min(A) - 1
    lr = [[i - 1 - minA, i + 1 - minA] for i in A]
    lst = [0] * (max(A) - minA + 3)
    for i, j in lr:
        lst[i] += 1
        lst[j + 1] -= 1
    lst = list(accumulate(lst))
    print(max(lst))


if __name__ == '__main__':
    main()
