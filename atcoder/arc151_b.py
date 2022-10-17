# https://atcoder.jp/contests/arc151/tasks/arc151_b
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)
MOD = 998244353

def main():
    N, M = map(int, input().split())
    P = [int(x)-1 for x in input().split()]
    ans = pow(M, N, MOD)
    done = [False]*N
    same = 1
    for i in range(N):
        if done[i]: continue
        same *= M
        same %= MOD
        now = i
        while done[now] is False:
            done[now] = True
            now = P[now]    
    ans -= same
    ans %= MOD
    ans *= pow(2, MOD-2, MOD)
    ans %= MOD
    print(ans)
    return

main()



# import sys
# input = sys.stdin.buffer.readline
# # sys.setrecursionlimit(10 ** 7)
# MOD = 998244353

# class UnionFind():
#     """ Union-Find木の実装（ランクあり） """
#     def __init__(self, n):
#         self.n = n
#         self.parent = [-1]*(n+1)    # parent 親 マイナスだったら根で、絶対値が集合の数
#         self.rank   = [0]*(n+1)     # rank 深さ

#     def root(self, x):
#         """ 木の根を求める """
#         if self.parent[x] < 0:      # xが根
#             return x
#         else:
#             self.parent[x] = self.root(self.parent[x])  # 経路圧縮
#             return self.parent[x]
            
#     def unite(self, x, y):
#         """ xとyの属する集合を併合 """
#         x = self.root(x)
#         y = self.root(y)
#         if x == y:
#             return 0
#         elif self.rank[x] > self.rank[y]:
#             self.parent[x] += self.parent[y]
#             self.parent[y] = x
#         else:
#             self.parent[y] += self.parent[x]
#             self.parent[x] = y
#             if self.rank[x] == self.rank[y]:
#                 self.rank[y] += 1

#     def isSame(self, x, y):
#         """ xとyが同じ集合に属するか否か """
#         return self.root(x) == self.root(y) or x==y
    
#     def size(self, x):
#         """ xと同じ集合に属する数 """
#         return -self.parent[self.root(x)]

# def main():
#     N, M = map(int, input().split())
#     P = list(map(int, (input().split())))
#     rest = N
#     ans = 0
#     done = [False] * N
#     pairs = 0
#     uf = UnionFind(N)

#     for i in range(N-1):
#         # print(done[i], done[P[i]-1])
#         if done[i] is False and done[P[i]-1] is False:
#             pairs += 1
#         if done[i] and done[P[i]-1] and uf.isSame(i, P[i]-1) is False:
#             pairs -= 1
#         uf.unite(i, P[i]-1)
#         print(i, P[i]-1, pairs)
#         if done[i] and done[P[i]-1]: continue
#         if i==P[i]-1:
#             done[i] = True
#             rest -= 1
#         else:
#             tmp = pow(M, pairs - 1, MOD)
#             if done[i] is False:
#                 done[i] = True
#                 rest -= 1
#             if done[P[i]-1] is False:
#                 done[P[i]-1] = True
#                 rest -= 1
#             tmp *= M*(M-1)//2
#             tmp *= pow(M, rest, MOD)
#             tmp %= MOD
#             ans += tmp
#             ans %= MOD
#         print(i, P[i]-1, rest, tmp, ans)
#         if rest<=1: break
#     print(ans)
#     return

# main()


# S = input()
# n = int(input())
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]

# import sys
# it = map(int, sys.stdin.buffer.read().split())
# N = next(it)

# @njit('(i8,i8[::1],i4[::1])', cache=True)
# def main():
#     @lru_cache(None)
#     def dfs():
#         return
#     return

# main()
