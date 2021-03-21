# https://atcoder.jp/contests/abc135/tasks/abc135_b

N = int(input())
p = list(map(int, input().split()))

cnt = 0
for i in range(N):
    if p[i] != i+1:
        cnt += 1

if cnt > 2:
    print('NO')
else:
    print('YES')
