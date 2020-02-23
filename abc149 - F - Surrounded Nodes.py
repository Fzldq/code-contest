# https://atcoder.jp/contests/abc149/tasks/abc149_f

import io

s = '''7
4 7
3 1
2 6
5 2
7 1
2 7
'''
f = io.StringIO(s)
readline = f.readline

N = int(readline())
graph = [[] for _ in range(N + 1)]
for i in range(N - 1):
    a, b = map(int, readline().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [0] * (N + 1)
order = []
stack = [1]
while stack:
    x = stack.pop()
    order.append(x)
    for y in graph[x]:
        if y == parent[x]:
            continue
        parent[y] = x  # 记录爸爸
        stack.append(y)

MOD = 10**9 + 7
half = pow(2, MOD - 2, MOD)
power_inv = [1] * (N + 1)
size = [1] * (N + 1)
for i, v in enumerate(order[::-1], 1):
    p = parent[v]
    x = size[v]  # vの子孫ノード数（自分も含む）をとる
    size[p] += x  # 親にノード数を加算
    power_inv[i] = power_inv[i - 1] * half % MOD  # [1, 1/2, 1/4, ...]

ans = sum((1 - power_inv[i] - power_inv[N - i] + power_inv[N]) %
          MOD for i in size[2:])  # 解法1の確率式：辺iがSに含まれるための必要十分条件
ans += 1  # 木の頂点の個数は(空グラフの場合を除き)辺の個数+1
ans -= power_inv[N] + N * power_inv[1]  # -「空グラフでない」-N/2
ans %= MOD

print(ans)
