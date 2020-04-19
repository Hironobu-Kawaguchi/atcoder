# https://atcoder.jp/contests/abc147/tasks/abc147_d
import sys
# input = sys.stdin.buffer.readline
def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 7)

MOD = 10**9+7

N = int(input())
A = list(map(int, (input().split())))

ans = 0
for i in range(60):
    zero, one = 0, 0
    for j in range(N):
        if A[j]>>i&1:
            one += 1
        else:
            zero += 1
    ans += (one * zero)<<i
    ans %= MOD
print(ans)

# ans = 0
# for i in range(N):
#     for j in range(i, N):
#         ans += A[i] ^ A[j]
#         ans %= MOD
# print(ans)
