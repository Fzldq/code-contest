# https://atcoder.jp/contests/past-sample/tasks/abc129_d

import numpy as np
import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines

# H,W = map(int,readline().split())
# grid = np.frombuffer(read(),'S1').reshape(H,-1)[:,:W]

grid = np.array([[b'#', b'.', b'.', b'#', b'.', b'.'],
                 [b'.', b'.', b'.', b'.', b'.', b'#'],
                 [b'.', b'.', b'.', b'.', b'#', b'.'],
                 [b'#', b'.', b'#', b'.', b'.', b'.']]
                )


def cnt_U(grid):
    H, W = grid.shape
    wall = (grid == b'#')
    floor = ~wall
    U = np.zeros((H, W), np.int32)
    for h in range(H):
        if h != 0:
            U[h] = U[h - 1]
        U[h] += 1
        U[h] *= floor[h]
    return U


x = cnt_U(grid) + cnt_U(grid[::-1])[::-1]
grid = grid.T
y = cnt_U(grid) + cnt_U(grid[::-1])[::-1]
x += y.T
answer = x.max() - 3
print(answer)
