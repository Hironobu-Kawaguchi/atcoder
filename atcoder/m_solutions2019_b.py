# B - Sumo
# https://atcoder.jp/contests/m-solutions2019/tasks/m_solutions2019_b

S = input()
n = len(S)

cnt = 0
for i in range(n):
    if S[i] == 'o':
        cnt += 1
cnt += 15 - n
if cnt >= 8:
    print('YES')
else:
    print('NO')
