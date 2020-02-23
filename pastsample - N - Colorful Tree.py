# https://atcoder.jp/contests/past-sample/tasks/abc133_f

import io
import numpy as np

a = '''5 3
1 2 1 10
1 3 2 20
2 4 4 30
5 2 1 40
1 100 1 4
1 100 1 5
3 1000 3 4
'''
f = io.StringIO(a)

# まずはLCAの頂点の計算に専念する

N, Q = map(int, f.readline().split())
m = map(int, f.read().split())
data = list(zip(m, m, m, m))
ABCD = data[:N - 1]
XYUV = data[N - 1:]
graph = [[] for _ in range(N + 1)]
for a, b, c, d in ABCD:
    graph[a].append((b, c, d))
    graph[b].append((a, c, d))


def EulerTour(graph, start=1):
    """
    1-indexed graph
    graphを破壊しているので場合によっては注意
    """
    V = len(graph)
    par = [0] * V
    depth = [0] * V
    depth[start] = 0
    color = [0] * V
    length = [0] * V
    tour = [start]
    st = [start]
    while st:
        x = st[-1]
        if not graph[x]:
            st.pop()
            tour.append(par[x])
            continue
        y, c, d = graph[x].pop()
        if y == par[x]:
            continue
        par[y] = x
        color[y] = c
        length[y] = d
        depth[y] = depth[x] + 1
        st.append(y)
        tour.append(y)
    return tour, depth, color, length


tour, depth, color, length = EulerTour(graph)
Ltour = len(tour)
tour_arr = np.array(tour)
depth_arr = np.array(depth)
tour_d = depth_arr[tour_arr]

idx = np.arange(len(depth))
idx[tour_arr] = np.arange(Ltour)

# depth最小を実現するインデックスのsparse tableを作る
sp = np.empty((Ltour.bit_length(), Ltour), np.int32)
sp[0] = np.arange(Ltour)
for n in range(1, Ltour.bit_length()):
    prev, width = sp[n - 1], 1 << (n - 1)
    x = prev[:-width]
    y = prev[width:]
    condition = tour_d[x] > tour_d[y]
    sp[n] = prev
    sp[n, :-width][condition] = y[condition]


def LCA(A, B):
    AB = np.vstack([A, B]).T
    LR = idx[AB]
    LR.sort(axis=1)
    # [L,R] におけるRmQ
    L = LR[:, 0]
    R = LR[:, 1]
    x = R - L
    n = np.zeros_like(x)  # 2^n <= R-L
    for _ in range(20):
        x >>= 1
        n[x > 0] += 1
    x = sp[n, L]
    y = sp[n, R - (1 << n) + 1]
    return np.where(tour_d[x] < tour_d[y], tour_arr[x], tour_arr[y])


X, Y, U, V = zip(*XYUV)
W = LCA(U, V).tolist()

add = [[] for _ in range(N + 1)]
sub = [[] for _ in range(N + 1)]
for i, ((x, y, u, v), w) in enumerate(zip(XYUV, W)):
    add[u].append([i, x, y])  # 色xをyにしたときの距離をiに加算
    add[v].append([i, x, y])  # 色xをyにしたときの距離をiに加算
    sub[w].append([i, x, y])  # 2倍を引く
graph = [[] for _ in range(N + 1)]
for a, b, c, d in ABCD:
    if depth[a] < depth[b]:
        graph[a].append((b, c, d))
    else:
        graph[b].append((a, c, d))
# euler tourをもう1周しながらあれこれ
answer = [0] * Q
col_cnt = [0] * (N + 1)  # 色ごとの距離の和
col_sum = [0] * (N + 1)  # 色ごとの距離の和
total = 0
prev = 0
print('tour', tour)
print('depth', depth)
print('color', color)
print('length', length)
for v in tour:
    if depth[prev] < depth[v]:
        c = color[v]
        d = length[v]
        col_cnt[c] += 1
        col_sum[c] += d
        total += d
        # ここでクエリ処理
        for i, x, y in add[v]:
            L = total - col_sum[x] + col_cnt[x] * y
            answer[i] += L
        for i, x, y in sub[v]:
            L = total - col_sum[x] + col_cnt[x] * y
            answer[i] -= L + L
    else:
        c = color[prev]
        d = length[prev]
        col_cnt[c] -= 1
        col_sum[c] -= d
        total -= d
    prev = v

print('\n'.join(map(str, answer)))
