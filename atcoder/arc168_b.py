# https://atcoder.jp/contests/arc168/tasks/arc168_b
# from numba import njit
# from functools import lru_cache

import sys
# input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

from collections import Counter

N = int(input())
A = list(map(int, (input().split())))
cntA = Counter(A)

xor = 0
for a in A:
    xor ^= a

if xor != 0:    # 0以外の場合は，全てのkでAliceが勝つ
    print(-1)
else:           # grundy数は，A_i mod (k+1) 
    for a, v in sorted(cntA.items(), reverse=True):
        if v % 2:   # 奇数個の場合は，K=a-1でgrundy数のXORが0以外になるため必勝
            print(a - 1)
            break
    else:       # 全てが偶数個の場合は，grundy数のXORが0になるため，必勝法なし
        print(0)



# WA
# N = int(input())
# A = list(map(int, (input().split())))

# xor = 0
# for a in A:
#     print(a, bin(a), bin(~a & (1 << a.bit_length()) - 1), file=sys.stderr)
#     xor ^= a
# print(xor, bin(xor), file=sys.stderr)

# if xor != 0:    # 0以外の場合は，全てのkでAliceが勝つ
#     print(-1)
#     exit()

# # 最大値が偶数ある場合は，必勝法なし
# max_a = max(A)
# cnt = 0
# for a in A:
#     if a == max_a:
#         cnt += 1
# if cnt % 2 == 0:
# # if cnt >= 2:
#     print(0)
#     exit()

# # 0の場合は，Aliceが勝つkを探す
# k = 0
# for a in A:
#     k = max(k, (~a & (1 << a.bit_length()) - 1) + 1)
# print(k)
