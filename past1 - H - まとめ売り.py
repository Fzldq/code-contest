# https://atcoder.jp/contests/past201912-open/tasks/past201912_h

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n = int(readline())
odd = n // 2 + n % 2
goods = [int(i) for i in readline().split()]
mingoods = min(goods)
minodd = min(goods[i] for i in range(0, n, 2))
_, *orders = readlines()
res = 0
o = 0
a = 0
dic = {}
for i in orders:
    num, *order = map(int, i.strip().split())

    if num == 1:
        order0 = order[0]
        order1 = order[1]
        if order0 % 2:
            if order0 in dic:
                goods[order0 - 1] -= (o - dic[order0][0])
                dic[order0][0] = o
            else:
                goods[order0 - 1] -= o
                dic[order0] = [o, 0]
        if order0 in dic:
            goods[order0 - 1] -= (a - dic[order0][1])
            dic[order0][1] = a
        else:
            goods[order0 - 1] -= a
            dic[order0] = [0, a]

        if goods[order0 - 1] >= order1:
            goods[order0 - 1] -= order1
            tmp = goods[order0 - 1]
            res += order1
            if mingoods > tmp:
                mingoods = tmp
            if order0 % 2 == 1 and minodd > tmp:
                minodd = tmp

    elif num == 2:
        order0 = order[0]
        if minodd >= order0:
            o += order0
            res += order0 * odd
            minodd -= order0
            if mingoods > minodd:
                mingoods = minodd

    elif num == 3:
        order0 = order[0]
        if mingoods >= order0:
            a += order0
            res += order0 * n
            mingoods -= order0
            minodd -= order0
print(res)
