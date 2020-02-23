import matplotlib.pyplot as plt
import numpy as np


def chouka(c, count, nian, a):
    """
    c：抽卡次数
    count：保底
    nian，a：年，阿个数
    """
    c += 1
    if count > 50:
        p = count - 49
    else:
        p = 1
    t = np.random.rand()  # 生成一个在[0, 1)上一样分布的小数
    if t < 0.02 * p:
        count = 1
        if t < 0.007 * p:
            nian += 1
        elif t < 0.014 * p:
            a += 1
    else:
        count += 1
    return c, count, nian, a


ex = []
for _ in range(10000):
    c = nian = a = 0
    count = 1
    while nian < 1 or a < 1:
        c, count, nian, a = chouka(c, count, nian, a)
    ex += [c]
print(np.mean(ex))
plt.hist(ex)
plt.title('e={0:.2f}, var={1:.2f}'.format(np.mean(ex), np.var(ex)))
plt.show()
