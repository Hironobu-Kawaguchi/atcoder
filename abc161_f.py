# https://atcoder.jp/contests/abc161/tasks/abc161_f
# N, N-1, N-1の約数, Nの約数でchk通るもの
import sys
def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 7)

N = int(input())

def chk(K):
    n = N
    while n >= K:
        if n%K:
            n %= K
        else:
            n //= K
    if n == 1:
        return True
    else:
        return False

ans = set([N-1, N])

for i in range(2, int(N**0.5)+1):
    if N%i==0:
        if chk(i):
            ans.add(i)
        j = N//i
        if chk(j):
            ans.add(j)
    elif (N-1)%i==0:
        if chk(i):
            ans.add(i)
        j = (N-1)//i
        if chk(j):
            ans.add(j)

# print(ans)
if N == 2:
    print(1)
else:
    print(len(ans))

# TLE
# N = int(input())
# def chk(K):
#     n = N
#     while n >= K:
#         if n%K:
#             n -= K
#         else:
#             n //= K
#     if n == 1:
#         return True
#     else:
#         return False
# ans = 0
# ks = []
# for K in range(2, N+1):
#     if chk(K):
#         ans += 1
#         ks.append(K)
# print(ks)
# print(ans)



# N, K, C = map(int, input().split())
# S = input()
# A = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
