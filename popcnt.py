import numpy as np
import timeit


a = np.random.binomial(1, 0.5, size=(10, 256))
inta = [int(''.join(list(map(lambda x: str(int(x)), list(aa)))), 2)
        for aa in a]


def popcnt(n):
    c = (n & 0x5555555555555555555555555555555555555555555555555555555555555555) + \
        ((n >> 1) & 0x5555555555555555555555555555555555555555555555555555555555555555)
    c = (c & 0x3333333333333333333333333333333333333333333333333333333333333333) + \
        ((c >> 2) & 0x3333333333333333333333333333333333333333333333333333333333333333)
    c = (c & 0x0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f) + \
        ((c >> 4) & 0x0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f)
    c = (c & 0x00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff) + \
        ((c >> 8) & 0x00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff)
    c = (c & 0x0000ffff0000ffff0000ffff0000ffff0000ffff0000ffff0000ffff0000ffff) + \
        ((c >> 16) & 0x0000ffff0000ffff0000ffff0000ffff0000ffff0000ffff0000ffff0000ffff)
    c = (c & 0x00000000ffffffff00000000ffffffff00000000ffffffff00000000ffffffff) + \
        ((c >> 32) & 0x00000000ffffffff00000000ffffffff00000000ffffffff00000000ffffffff)
    c = (c & 0x0000000000000000ffffffffffffffff0000000000000000ffffffffffffffff) + \
        ((c >> 64) & 0x0000000000000000ffffffffffffffff0000000000000000ffffffffffffffff)
    c = (c & 0x00000000000000000000000000000000ffffffffffffffffffffffffffffffff) + \
        ((c >> 128) & 0x00000000000000000000000000000000ffffffffffffffffffffffffffffffff)
    return c


def count(n):
    c = 0
    while n:
        if n & 1:
            c += 1
        n >>= 1
    return c


def solution(inta, func=count):
    for i in inta:
        func(i)
    print('func is', func.__name__)


print(timeit.timeit('solution(inta)', number=1, globals=globals(
)) / timeit.timeit('solution(inta, func=popcnt)', number=1, globals=globals()))
