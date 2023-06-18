# https://atcoder.jp/contests/abc301/tasks/abc301_c
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

atcoder = 'atcoder'
S = input()
T = input()
scnt = [0]*27
for s in S:
    if s=='@':
        scnt[26] += 1
    else:
        scnt[ord(s)-ord('a')] += 1
tcnt = [0]*27
for t in T:
    if t=='@':
        tcnt[26] += 1
    else:
        tcnt[ord(t)-ord('a')] += 1
ans = 'Yes'
for i in range(26):
    # print(ans, i, scnt, tcnt)
    if scnt[i]!=tcnt[i] and chr(i+ord('a')) not in atcoder:
        ans = 'No'
        # print("A")
        break
    elif scnt[i]<tcnt[i]:
        if scnt[26]>=tcnt[i]-scnt[i]:
            scnt[26] -= tcnt[i]-scnt[i]
        else:
            ans = 'No'
            # print("B")
            break
    elif scnt[i]>tcnt[i]:
        if tcnt[26]>=scnt[i]-tcnt[i]:
            tcnt[26] -= scnt[i]-tcnt[i]
        else:
            ans = 'No'
            # print("C")
            break
print(ans)


# S = input()
# N = int(input())
# N, K = map(int, input().split())
# A = list(map(int, (input().split())))
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
