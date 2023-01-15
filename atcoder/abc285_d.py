# https://atcoder.jp/contests/ABC285/tasks/abc285_d
# from numba import njit
# from functools import lru_cache

import sys
# input = sys.stdin.buffer.readline
def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 7)

N = int(input())

d = {}
idx = 0
lst = []
S, T = [], []
s_set, t_set = set(), set()
for i in range(N):
    s, t = input().split()
    S.append(s)
    s_set.add(s)
    T.append(t)
    t_set.add(t)
    if s not in d:
        d[s] = idx
        idx += 1
        lst.append(s)
    if t not in d:
        d[t] = idx
        idx += 1
        lst.append(t)
G = [[] for _ in range(len(lst))]
for i in range(N):
    G[d[S[i]]].append(d[T[i]])
# print(G)

s_t_set = s_set - t_set
# print(s_t_set)
if len(s_t_set)==0:
    ans = "No"
else:
    ans = "Yes"

visited = [False] * len(lst)

def dfs(pos):
    if visited[pos]:
        global ans
        ans = "No"
        return
    visited[pos] = True
    for v in G[pos]:
        dfs(v)
    return

for c in s_t_set:
    idx = d[c]
    if visited[idx]==False:
        dfs(idx)
for i in range(len(lst)):
    if visited[i]==False:
        dfs(i)

print(ans) 
