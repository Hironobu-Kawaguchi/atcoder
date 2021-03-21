# https://atcoder.jp/contests/dwacon5th-prelims/tasks/dwacon5th_prelims_a
import sys
input = sys.stdin.buffer.readline

N = int(input())
a = list(map(int, (input().split())))

sm = sum(a)
best_dif = 100*100
for i in range(N):
    dif = abs(a[i]*N - sm)
    if dif < best_dif:
        best_dif = dif
        ans = i
print(ans)
