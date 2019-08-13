# https://atcoder.jp/contests/abc060/tasks/arc073_a

N, T = map(int, input().split())
t = list(map(int, input().split()))

ans = T
for i in range(N-1):
    ans += min(t[i+1] - t[i], T)

print(ans)
