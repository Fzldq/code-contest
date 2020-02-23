import numpy as np
import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N = int(readline())
graph = [[] for _ in range(N + 1)]
for i in range(N):
    b = int(readline())
    graph[i + 1].append(b)
    graph[b].append(i + 1)


def EulerTour(graph, start=1):
    """
    1-indexed graph
    graphを破壊しているので場合によっては注意
    """
    V = len(graph)
    par = [0] * V
    depth = [0] * V
    depth[start] = 0
    tour = [start]
    st = [start]
    while st:
        x = st[-1]
        if not graph[x]:
            st.pop()
            tour.append(par[x])
            continue
        y = graph[x].pop()
        if y == par[x]:
            continue
        par[y] = x
        depth[y] = depth[x] + 1
        st.append(y)
        tour.append(y)
    return tour, depth


tour, depth = EulerTour(graph)
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
