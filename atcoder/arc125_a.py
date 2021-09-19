# https://atcoder.jp/contests/arc125/tasks/arc125_a
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)




N, M = map(int, input().split())
S = list(map(int, (input().split())))
T = list(map(int, (input().split())))
cnt = [0]*2
for i in range(N):
    cnt[S[i]] += 1
diff = -1
if cnt[0]!=0 or cnt[1!=0]:
    for i in range(1,N):
        if S[i]!=S[0]:
            diff = i
            break
    for i in range(N-1, 0, -1):
        if S[i]!=S[0]:
            diff = min(diff, N-i)
            break
now = S[0]
ans = 0
for i in range(M):
    if T[i]!=now:
        if diff==-1:
            ans = -1
            break
        ans += diff
        diff = 1
        now = T[i]
    ans += 1
    # print(i, ans)
print(ans)



# def next_search(si):
#     diff = -1
#     ni = -1
#     if cnt[0]==0 or cnt[1]==0:
#         return diff
#     for i in range(1,N):
#         if S[(i+si)%N]!=S[si]:
#             diff = (i-si+N)%N
#             ni = i
#             break
#     for i in range(N-1, 0, -1):
#         if S[(i+si)%N]!=S[si]:
#             if diff<(si+N-i)%N:
#             diff = min()
#             break
#     return diff



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
