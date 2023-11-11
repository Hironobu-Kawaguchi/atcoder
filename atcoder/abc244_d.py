# https://atcoder.jp/contests/abc244/tasks/abc244_d
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

d = {'R': 0, 'G': 1, 'B': 2}
S = list(input().split())
T = list(input().split())

# 転倒数を求める
def inversions(s):
    ret = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if d[s[i]] > d[s[j]]:
                ret += 1
    return ret

s_inv = inversions(S)
t_inv = inversions(T)

if s_inv % 2 == t_inv % 2:
    print('Yes')
else:
    print('No')




# 交互に可能な組み合わせが入れ替わることを確認
# from collections import defaultdict

# def swap_tuple(s, i, j):
#     ret = list(s)
#     ret[i], ret[j] = ret[j], ret[i]
#     return tuple(ret)

# S = tuple(input().split())
# T = tuple(input().split())

# num_iter = 10
# cnt = [defaultdict(int) for _ in range(num_iter+1)]
# cnt[0][S] = 1

# for it in range(num_iter):
#     for k, v in cnt[it].items():
#         for i, j in [(0, 1), (1, 2), (0, 2)]:
#             cnt[it+1][swap_tuple(k, i, j)] += v

# for it in range(num_iter+1):
#     print(it, *cnt[it].items())
