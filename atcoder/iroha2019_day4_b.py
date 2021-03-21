# B - 叫び声
# https://atcoder.jp/contests/iroha2019-day4/tasks/iroha2019_day4_b


N, M, L = map(int, input().split())

ans = M * L
for i in range(N):
    a, b = map(int, input().split())
    ans = min(a + b * M, ans)

print(ans)
