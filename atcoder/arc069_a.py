# https://atcoder.jp/contests/abc055/tasks/arc069_a

N, M = map(int, input().split())    # N:Sの数, M:cの数

if M > N * 2:
    tmp = (M - N * 2) // 4   # tmp:Sをcから作る数
else:
    tmp = 0
ans = min(N, M//2) + tmp
print(ans)
