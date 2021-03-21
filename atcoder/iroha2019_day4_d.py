# D - 揺れる街、増える敵
# https://atcoder.jp/contests/iroha2019-day4/tasks/iroha2019_day4_d
#  9 -> 4*4=16
# 10 -> 4*5=20, 2*3*3=18
# 11 -> 5*5=25, 3*3*3=27
# 12 -> 5*6=30, 3*3*4=36
# 13 -> 6*6=36, 3*4*4=48
# log4(2**A) = A/2 -> A/2 * 5 - 1

T = int(input())

for i in range(T):
    L, A = map(int, input().split())
    ans = min(max(int(L - (A/2 * 5 - 2)), 0), L)
    print(ans)
