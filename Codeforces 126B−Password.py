# http://codeforces.com/problemset/problem/126/B


def Z_algorithm(s):
    n = len(s)
    z = [0] * n
    l, r = 0, 0
    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i - 1, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1
    return z


s = 'fixprefixprsuffixp'

z = Z_algorithm(s)
print(z)
n = len(s)
z_max = max(z)
for i in range(n):
    if z_max >= z[i] == n - i:
        p = i
        break
print(s[i:])

print(Z_algorithm('ioioi'))
