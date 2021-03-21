# https://atcoder.jp/contests/abc143/tasks/abc143_d

import bisect

N = int(input())
L = list(map(int, input().split()))
L.sort()

ans = 0
for i in range(N-2):
    a = L[i]
    for j in range(i+1, N-1):
        b = L[j]
        ans += bisect.bisect_left(L, a+b) - j - 1

print(ans)
