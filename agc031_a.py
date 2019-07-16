# A - Colorful Subsequence
# https://atcoder.jp/contests/agc031/tasks/agc031_a

n = int(input())
s = input()
ans = 1
mod = 10**9 + 7
for x in set(s):
    ans *= s.count(x) + 1
    ans %= mod

print((ans - 1) % mod)

"""
n = int(input())
s = input()
csum = [1]

for i in range(1, n):
    if s[i] in s[:i]:
        csum.append(int(csum[-1] * 1.5 + 0.5))
    else:
        csum.append(csum[-1] * 2 + 1)

print(csum[-1])
"""