# https://atcoder.jp/contests/typical90/tasks/typical90_cg

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)
vec = []

K = int(input())
for i in range(1, int(K**0.5)+1):
    if K%i==0:
        vec.append(i)
        if K//i!=i:
            vec.append(K//i)
vec.sort()
# print(vec)

ans = 0
for i in range(len(vec)):
    for j in range(i, len(vec)):
        a = vec[i]
        b = vec[j]
        if K%(a*b): continue
        c = K // (a * b)
        if c<b: continue
        # print(a, b, c)
        ans += 1
print(ans)


# from collections import defaultdict
# prime_factor = defaultdict(int)
# for i in range(2, int(N**0.5)+1):
#     while N%i==0:
#         prime_factor[i] += 1
#         N //= i
# if N>1:
#     prime_factor[N] += 1
# print(prime_factor)

# ans = 1
# for k, v in prime_factor.items():
#     ans *= (v+1)*(v+1)
# ans //= 6
# print(ans)

