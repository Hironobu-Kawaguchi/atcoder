# https://atcoder.jp/contests/abc313/tasks/abc313_d

import sys
import copy
import random

# MAX_A = 10**9
# MAX_A = 2
MAX_A = random.choice([2, 3, 4, 10**9])
H = random.randint(2, 5)
W = random.randint(2, 5)
A = [[random.randint(1, MAX_A) for _ in range(W)] for _ in range(H)]
B = copy.deepcopy(A)
for iter in range(10):
    i = random.randint(0, H-2)
    for j in range(W):
        B[i][j], B[i+1][j] = B[i+1][j], B[i][j]
for iter in range(10):
    j = random.randint(0, W-2)
    for i in range(H):
        B[i][j], B[i][j+1] = B[i][j+1], B[i][j]

print(H, W)
for i in range(H):
    print(*A[i])
for i in range(H):
    print(*B[i])


# N = 250000
# # N = 10
# A = [random.randint(1, 10**9) for _ in range(N-1)]
# xor = 0
# for a in A:
#     xor ^= a
# A.append(xor)

# print(N)
# print(*A)



# N, K = 10, 5
# print(N, K)
# # print(N, K, file=sys.stderr)
# A = [random.randint(0, 1) for _ in range(N)]
# print(*A, file=sys.stderr)

# while True:
#     line = input()
#     c, x = line[0], line[2:]
#     x = list(map(int, x.split()))
#     if c=="?":
#         res = 0
#         for i in x:
#             res ^= A[i-1]
#         print(res)
#     else:
#         assert x == A, "Wrong Answer"
#         break
