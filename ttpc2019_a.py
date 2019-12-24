# https://atcoder.jp/contests/ttpc2019/tasks/ttpc2019_a

A, B, T = map(int, input().split())
ans = ((T-A-1)//(B-A)) * (B-A) + B
print(ans)
