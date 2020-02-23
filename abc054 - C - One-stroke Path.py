# https://atcoder.jp/contests/abc054/tasks/abc054_c

N, M = map(int, input().split())
graph = [[] for i in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

memo = {}
all_use = (1 << N) - 1


def rec(v, use):
    if use == all_use:
        return 1

    key = (v, use)
    if key in memo:
        return memo[key]

    res = 0
    for u in graph[v]:
        if (use >> u) & 1 == 1:
            continue

        use ^= 1 << u
        res += rec(u, use)
        use ^= 1 << u

    memo[key] = res
    return res


print(rec(0, 1))
