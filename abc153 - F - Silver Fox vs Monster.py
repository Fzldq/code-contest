# https://atcoder.jp/contests/abc153/tasks/abc153_f

import io
from collections import deque

s = '''3 3 2
1 2
5 4
12 5
'''
f = io.StringIO(s)
n, d, a = map(int, f.readline().split())
m = map(int, f.read().split())
monsters = sorted(zip(m, m), key=lambda x: x[0])

bomb_area = deque([])
bomb_power = deque([])
total_damage = 0
ans = 0
for pos, hp in monsters:
    while bomb_area:
        print(bomb_area, bomb_power, total_damage)
        area = bomb_area[0]
        if area < pos:
            bomb_area.popleft()
            power = bomb_power.popleft()
            total_damage -= power
            print(total_damage)
        else:
            break
    if hp <= total_damage:
        continue
    else:
        rest = hp - total_damage
        count = rest // a + (rest % a != 0)
        ans += count
        power = a * count
        total_damage += power
        bomb_area.append(pos + 2 * d)
        bomb_power.append(power)
print(ans)
