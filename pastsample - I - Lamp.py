# https://atcoder.jp/contests/past-sample/tasks/abc129_d

import numpy as np
import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# H,W = map(int,readline().split())
# grid = np.frombuffer(read(),'S1').reshape(H,-1)[:,:W]

grid = np.array([[b'#', b'.', b'.', b'#', b'.', b'.'],
                 [b'.', b'.', b'.', b'.', b'.', b'#'],
                 [b'.', b'.', b'.', b'.', b'#', b'.'],
                 [b'#', b'.', b'#', b'.', b'.', b'.']]
                )
print(grid.dtype)


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


print(grid)
x = cnt_U(grid) + cnt_U(grid[::-1])[::-1]
print(x)
grid = grid.T
print(grid)
y = cnt_U(grid) + cnt_U(grid[::-1])[::-1]
print(y)
x += y.T
print(x)
answer = x.max() - 3
print(answer)
