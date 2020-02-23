from math import factorial  # 阶乘函数
import matplotlib.pyplot as plt

Expect = 0  # 抽到6星的期望次数
q = 0.98
for i in range(1, 51):  # 前50次
    Expect += 0.02 * i * pow(q, i - 1)

prep = 0.98
for i in range(51, 100):  # 51~99次
    p = 0.02 * (i - 49)
    Expect += pow(0.98, 49) * i * p * prep
    prep *= 1 - p  # 没抽到的概率，用于计算下一次抽卡


def comb(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))


res = 0  # 2个角色都抽到满破的期望6星个数
lst = []  # 用于保存各轮概率的空列表
tmp = 0  # 临时变量，跑完一次要重置成0

# 抽到6星的情况下，2个角色都抽到满破的次数n，大等于12。100次之后的概率忽略不计了
for n in range(12, 100):
    # n-6次中抽到0~5个角色2的概率和
    for m in range(6):
        tmp += comb(n - 6, m) * pow(0.35, m) * pow(0.3, n - 6 - m)
    # 最后一次一定抽到角色1，故要在前n-1次里选出5次抽到角色1，
    # 再在剩下的n-6次中抽到6次以上角色2
    # n-6次都抽不到角色1的概率 - n-6次中抽到0~5个角色2的概率和
    # = n-6次中抽到6次以上角色2
    # 最后一次抽到角色1或是角色2的情况是对称的，所以前面要乘2
    p = 2 * comb(n - 1, 5) * pow(0.35, 6) * (pow(0.65, n - 6) - tmp)

    lst += [p]
    res += n * p
    tmp = 0

res *= Expect  # 2个角色都抽到满破的期望6星个数*抽到6星的期望次数
print(res)

var = sum(pow(Expect * n - res, 2) * p for n, p in enumerate(lst, 12))
plt.plot(range(12, 100), lst)
plt.title('Expect={0:.2f}, Var={1:.2f}'.format(res, var))
plt.show()
