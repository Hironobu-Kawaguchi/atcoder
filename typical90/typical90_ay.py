# https://atcoder.jp/contests/typical90/tasks/typical90_ay

import sys
input = sys.stdin.buffer.readline
import bisect

N, K, P = map(int, input().split())
A = list(map(int, (input().split())))

def bit_search(start, num):
    ret = [[] for _ in range(num+1)]
    for bi in range(1<<num):
        k = 0
        p = 0
        for i in range(num):
            if bi>>i&1:
                k += 1
                p += A[start + i]
        ret[k].append(p)
    for i in range(num+1):
        ret[i].sort()
    return ret

B = bit_search(0, N//2)
# print(B)
C = bit_search(N//2, N - N//2)
# print(C)

ans = 0
for i in range(len(B)):
    for p in B[i]:
        if 0 <= K-i <= len(C)-1:
            ans += bisect.bisect_right(C[K-i], P-p)

print(ans)
