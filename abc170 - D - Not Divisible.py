# https://atcoder.jp/contests/abc170/tasks/abc170_d

import io

s = '''10
33 18 45 28 8 19 89 86 2 4
'''

f = io.StringIO(s)


def main():
    n, *A = map(int, f.read().split())
    m = max(A)
    lst = [0] * (m + 1)
    prep = 0
    for i in A:
        if i == prep:
            lst[i] += 1
            continue
        lst[2 * i::i] = [1] * len(lst[2 * i::i])
        prep = i
    res = 0
    for i in A:
        if lst[i] == 0:
            res += 1
    print(res)


if __name__ == '__main__':
    main()
