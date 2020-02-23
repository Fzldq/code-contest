# https://atcoder.jp/contests/past201912-open/tasks/past201912_k

import io
import numpy as np

input_data = '''20
4
11
12
-1
1
13
13
4
6
20
1
1
20
10
8
8
20
10
18
1
20
18 14
11 3
2 13
13 11
10 15
9 5
17 11
18 10
1 16
9 4
19 6
5 10
17 8
15 8
5 16
6 20
3 19
10 12
5 13
18 1
'''
f = io.StringIO(input_data)
N = int(f.readline())
graph = [[] for _ in range(N + 1)]
for i in range(N):
    b = int(f.readline())
    if b == -1:
        start = i + 1
    else:
        graph[b].append(i + 1)
Q = int(f.readline())
AB = np.int32(f.read().split())


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


tour, depth = EulerTour(graph, start)
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


A = AB[::2]
B = AB[1::2]

answer = np.where(LCA(A, B) == B, 'Yes', 'No')
print('\n'.join(answer))
