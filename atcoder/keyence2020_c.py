# https://atcoder.jp/contests/keyence2020/tasks/keyence2020_a

N, K, S = map(int, input().split())
if S == 10**9:
    tmp = 1
else:
    tmp = 10**9

ans = [S] * K + [tmp] * (N-K)
print(*ans)
