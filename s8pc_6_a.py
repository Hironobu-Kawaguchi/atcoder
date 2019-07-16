# A - E869120, who Leaps through Time
# https://atcoder.jp/contests/s8pc-6/tasks/s8pc_6_a

N, T = map(int, input().split())
A = list(map(int, input().split()))

print(-(-sum(A)//T))