# https://atcoder.jp/contests/abc172/tasks/abc172_d

import numba

@numba.njit
def main(n):
    ans = 0
    for k in range(1, n+1):
        for f in range(1,n//k+1):
            ans += k*f
    return ans

n = int(input())
print(main(n))

# S = input()
# n = int(input())
# N, K = map(int, input().split())
# l = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
