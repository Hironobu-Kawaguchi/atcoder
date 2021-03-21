# C - Unification
# https://atcoder.jp/contests/abc120/tasks/abc120_c

S = input()

c0 = S.count('0')
c1 = S.count('1')

print(len(S) - abs(c0 - c1))
