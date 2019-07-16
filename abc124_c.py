# C - Coloring Colorfully
# https://atcoder.jp/contests/abc124/tasks/abc124_c
"""
S = input()
N = len(S)
even = S[0::2]
odd = S[1::2]
ptn0 = N - (even.count('0') + odd.count('1'))
ptn1 = N - (even.count('1') + odd.count('0'))
print(min(ptn0, ptn1))
"""
S = input()
cnt = [[0,0],[0,0]]
for i, s in enumerate(S):
    x = int(i) % 2
    y = int(s)
    cnt[x][y] += 1
print(min(cnt[0][1] + cnt[1][0], cnt[0][0] + cnt[1][1]))
# if cnt[0][0] > cnt[1][0]:
#     print(cnt[0][1] + cnt[1][0])
# else:
#     print(cnt[0][0] + cnt[1][1])