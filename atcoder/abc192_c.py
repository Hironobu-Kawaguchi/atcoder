# https://atcoder.jp/contests/abc192/tasks/abc192_b
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

def g1(x):
    s = list(str(x))
    # print(s)
    ret = ''.join(sorted(s, reverse=True))
    return int(ret)

def g2(x):
    s = list(str(x))
    # print(s)
    ret = ''.join(sorted(s))
    return int(ret)

def f(x):
    return g1(x) - g2(x)

N, K = map(int, input().split())
ans = N
ans_list = [N]
ans_set = set([N])
for i in range(K):
    # print(ans)
    ans = f(ans)
    if ans in ans_set:
        for j, a in enumerate(ans_list):
            if a==ans: break
        start = j
        cycle = i+1-j
        idx = (K - start) % cycle + start
        ans = ans_list[idx]
        break
    ans_list.append(ans)
    ans_set.add(ans)
    if ans == 0: break
    # if ans == N: break
# print(ans_list)
print(ans)


# S = input()
# n = int(input())
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]

# @njit('(i8,i8[::1],i4[::1])', cache=True)
# def main():
#     @lru_cache(None)
#     def dfs():
#         return
#     return

# main()
