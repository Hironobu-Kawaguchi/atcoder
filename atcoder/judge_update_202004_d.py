# https://atcoder.jp/contests/judge-update-202004/tasks/judge_update_202004_d
import sys
def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 7)

import math

N, Q = map(int, input().split())
A = list(map(int, (input().split())))
S = list(map(int, (input().split())))

gcds = [A[0]]
for i in range(N-1):
    gcds.append(math.gcd(gcds[-1],A[i+1]))

for j in range(Q):
    last_gcd = math.gcd(gcds[-1], S[j])
    if last_gcd != 1:
        print(last_gcd)
    else:
        left = -1
        right = N
        while left+1 < right:
            i = (left + right) // 2
            now_gcd = math.gcd(gcds[i], S[j])
            if now_gcd == 1:
                right = i
            else:
                left = i
        print(right+1)

# S = input()
# N = int(input())
# S, L, R = map(int, input().split())
# A = [[int(i) for i in input().split()] for _ in range(N)]
