# https://atcoder.jp/contests/abc061/tasks/abc061_b

n, m = map(int, input().split())
cnt = [0] * n
for i in range(m):
    a, b = map(int, input().split())
    cnt[a-1] += 1
    cnt[b-1] += 1
for i in range(n):
    print(cnt[i])
