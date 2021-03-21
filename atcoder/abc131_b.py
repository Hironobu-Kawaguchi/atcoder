# https://atcoder.jp/contests/abc131/tasks/abc131_b

N, L = map(int, input().split())

ans = 0
for i in range(N):
    ans += L + i

if L > -1:
    ans -= L
elif L <= -N:
    ans -= L + N - 1

print(ans)
