# D - XXOR
# https://atcoder.jp/contests/abc117/tasks/abc117_d

import numpy as np
from functools import lru_cache

N,K = map(int,input().split())
A = np.array(input().split(),dtype=np.int64)

bit_cnt = [((A>>k)&1).sum() for k in range(50)]

# @lru_cache(maxsize = 10**6)
@lru_cache(maxsize = None)
def F(K,k = 49):
  # K以下、k-bit目まで見た(inclusive)の和、最大値
  if k == -1:
    return 0
  bit = 1<<k
  # k-bitを使う
  x = 0
  if K >= bit:
    x = ((N-bit_cnt[k])<<k) + F(K-bit,k-1)
  # k-bitを使わない
  y = (bit_cnt[k]<<k) + F(min(K,bit-1),k-1)
  return max(x,y)

answer = F(K)
print(answer)


# # WA
# N, K = map(int, input().split())
# A = list(map(int, input().split()))

# X = 0
# ans = 0
# # for i in range(40, -1, -1):
# for i in range(41):
#     bit = 1 << i
#     count = 0
#     for a in A:
#         if bit & a:
#             count += 1
#     if N >= count * 2 and (X^bit) <= K:
#         X ^= bit
#         count = N - count
#     ans += count * bit

# print(ans)


# WA https://atcoder.jp/contests/abc117/submissions/5221315

# import math
# N, K  = map(int, input().split())
# A = list(map(int, input().split()))
# if K == 0:
#     print(sum(A))
#     exit()
# else:
#     kk = int(math.log2(K)) + 1
# l1 = [0] * kk
# ok = 0

# for a in A:
#     bina = bin(a)[2:]
#     if len(bina) > kk:
#         binok = bina[:-kk]
#         ok += int(binok, 2)
#         bina = bina[-kk:]
#     for i in range(1, len(bina) + 1):
#         if bina[-i] == '1':
#             l1[-i] += 1

# ans = ok * 2 ** kk

# for j in range(kk):
#     ans += max(l1[j], N - l1[j]) * 2 ** (kk - j -1)

# print(ans)
