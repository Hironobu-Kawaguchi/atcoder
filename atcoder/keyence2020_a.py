# https://atcoder.jp/contests/keyence2020/tasks/keyence2020_a

H = int(input())
W = int(input())
N = int(input())

tmp = max(H, W)
ans = (N + tmp - 1) // tmp
print(ans)
