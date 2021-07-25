# https://atcoder.jp/contests/arc124/tasks/arc124_a
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

# import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

MOD = 998244353

N, K = map(int, input().split())
nums = []
st = K
for i in range(K):
    c, k = input().split()
    k = int(k)
    k -= 1
    if c=='L':
        st -= 1
        nums.append([k, +1])
    else:
        nums.append([k, -1])
nums.append([-1, st])
nums.sort()
for i in range(1, len(nums)):
    nums[i][1] += nums[i-1][1]
nums.append([N, 0])
# print(nums)
ans = 1
for i in range(len(nums)-1):
    if nums[i][0] + 1 == nums[i+1][0]: continue
    ans *= pow(nums[i][1], nums[i+1][0]-nums[i][0]-1, MOD)
    ans %= MOD
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
