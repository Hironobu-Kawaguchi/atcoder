# https://atcoder.jp/contests/abc130/tasks/abc130_b

N, X = map(int, input().split())
L = list(map(int, (input().split())))

ans = 1
sums = 0
for i in range(N):
    sums += L[i]
    if sums <= X:
        ans += 1

print(ans)
