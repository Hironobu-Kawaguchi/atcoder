# https://atcoder.jp/contests/keyence2020/tasks/keyence2020_a

# TLE
from itertools import permutations
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ans = -1

def chk(a):
    for i in range(N-1):
        if a[i] > a[i+1]:
            return False
    return True

def cnt(idx):
    res = 0
    for i in range(N):
        res += abs(idx[i] - i)
    return res // 2

for idx in permutations(range(N)):
    # print(idx)
    a = []
    for i in range(N):
        if (idx[i] % 2) ^ (i%2):
            a.append(B[idx[i]])
        else:
            a.append(A[idx[i]])
    # print(a)
    if chk(a):
        if ans == -1:
            ans = cnt(idx)
        else:
            ans = min(ans, cnt(idx))

print(ans)


# TLE
# from itertools import permutations
# N = int(input())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))
# ans = -1

# # def chk(a):
# #     for i in range(N-1):
# #         if a[i] > a[i+1]:
# #             return False
# #     return True

# def cnt(idx):
#     res = 0
#     for i in range(N):
#         res += abs(idx[i] - i)
#     return res // 2

# for idx in permutations(range(N)):
#     # print(idx)
#     a = []
#     flg = True
#     for i in range(N):
#         if (idx[i] % 2) ^ (i%2):
#             a.append(B[idx[i]])
#         else:
#             a.append(A[idx[i]])
#         if i and (a[i-1] > a[i]):
#             flg = False
#             break
#     # print(a)
#     if flg:
#         if ans == -1:
#             ans = cnt(idx)
#         else:
#             ans = min(ans, cnt(idx))

# print(ans)
