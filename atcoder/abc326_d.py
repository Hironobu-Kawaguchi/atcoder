# https://atcoder.jp/contests/abc326/tasks/abc326_d

import itertools
N = int(input())
R = input()
C = input()

def head(s):
    for c in s:
        if c != '.': 
            return c

for a, b, c in itertools.product(itertools.permutations(range(N)), repeat=3):
    if any(ai==bi or ai==ci or bi==ci for ai, bi, ci in zip(a, b, c)): continue
    # print(a, b, c)
    ans = [['.'] * N for _ in range(N)]
    for i, j in enumerate(a): ans[i][j] = 'A'
    for i, j in enumerate(b): ans[i][j] = 'B'
    for i, j in enumerate(c): ans[i][j] = 'C'
    if "".join(map(head, ans)) == R and "".join(map(head, zip(*ans))) == C:
        print("Yes")
        for i in range(N):
            print(''.join(ans[i]))
        exit()
print("No")



# import sys
# # input = sys.stdin.buffer.readline
# # def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

# N = int(input())
# R = input()
# C = input()

# ans = [['.'] * N for _ in range(N)]
# R_list = [[] for _ in range(N)]
# C_list = [[] for _ in range(N)]
# R_idx = [[] for _ in range(N)]
# C_idx = [[] for _ in range(N)]

# flg = False
# cnt = 0

# def dfs(v):
#     global flg, cnt
#     cnt += 1
#     if v == N*3:
#         flg = True
#         print("Yes")
#         for i in range(N):
#             print(''.join(ans[i]))
#         exit()
#         return
#     i = v // 3
#     # print(v, i, R_list[i], R_idx[i], C_list, C_idx, file=sys.stderr)
#     for c in ['A', 'B', 'C']:
#         if c in R_list[i]: continue
#         if len(R_list[i])==0 and R[i] != c: continue
#         l = 0
#         if len(R_idx[i])>0:
#             l = R_idx[i][-1] + 1
#         r = N - 3 + len(R_list[i])
#         for j in range(l, r+1):
#             # print(v, i, j, R_list[i], R_idx[i], C_list[j], C_idx[j], file=sys.stderr)
#             if c in C_list[j]: continue
#             if len(C_list[j])==0 and C[j] != c: continue
#             ans[i][j] = c
#             R_list[i].append(c)
#             R_idx[i].append(j)
#             C_list[j].append(c)
#             C_idx[j].append(i)
#             dfs(v+1)
#             ans[i][j] = '.'
#             R_list[i].pop()
#             R_idx[i].pop()
#             C_list[j].pop()
#             C_idx[j].pop()
#     return

# dfs(0)
# if not flg:
#     print("No")
# print(cnt, file=sys.stderr)
# # print(flg)
# # print(ans)
