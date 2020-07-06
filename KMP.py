# 返回全部匹配位置


def p_arr(p):
    n = len(p)
    arr = [0] * n
    arr[0] = -1
    k, j = -1, 0
    while j < n - 1:
        if k == -1 or p[j] == p[k]:
            j += 1
            k += 1
            arr[j] = k
        else:
            k = arr[k]
    return arr


def kmp(s, p):
    slen, plen = len(s), len(p)
    i, j = 0, 0
    arr = p_arr(p)
    lst = []
    while i < slen - 1 and j < plen:
        if j == -1 or s[i] == p[j]:
            i += 1
            j += 1
        else:
            j = arr[j]
        if j == plen:
            lst.append(i - j)
            i -= j - 1
            j = 0
    return lst


s, p = input().split()
print(kmp(s, p))
