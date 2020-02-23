# https://atcoder.jp/contests/past-sample/tasks/abc113_c

import io

s = '''2 3
1 32
2 63
1 12
000001000002
000002000001
000001000001
'''

f = io.StringIO(s)
n, m = map(int, f.readline().split())
py = map(int, f.read().split())
py = list(zip(py, py))
py = sorted(enumerate(py), key=lambda x: x[1])
dic = {}
ret = {}
for i, j in py:
    tp = j[0]
    if tp in dic:
        dic[tp] += 1
    else:
        dic[tp] = 1
    ps = str(tp).zfill(6)
    ns = str(dic[tp]).zfill(6)
    ret[i] = ps + ns
for i in ret.values():
    print(i)
