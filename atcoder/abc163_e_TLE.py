# https://atcoder.jp/contests/abc163/tasks/abc163_e

from itertools import permutations
N = int(input())
A = list(map(int, (input().split())))

ans = 0
for p in permutations(range(N)):
    tmp = 0
    for i in range(N):
        tmp += A[i] * abs(i-p[i])
    ans = max(ans, tmp)

print(ans)
