# https://atcoder.jp/contests/abc277/tasks/abc277_b
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

L1 = ['H' , 'D' , 'C' , 'S']
L2 = ['A' , '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9' , 'T' , 'J' , 'Q' , 'K']
st = set()

N = int(input())
S = [input() for _ in range(N)]
ans = "Yes"
for i in range(N):
    if S[i][0] not in L1:
        ans = "No"
        break
    if S[i][1] not in L2:
        ans = "No"
        break
    st.add(S[i])
if len(st)!=N:
    ans = "No"
print(ans)


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
