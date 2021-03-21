# https://atcoder.jp/contests/abc154/tasks/abc154_d

from functools import lru_cache
N = int(input())
K = int(input())

@lru_cache(None)
def f(N, K):
    if K == 0: return 1
    if N < 10:
        if K == 1: return N
        return 0
    q, r = divmod(N, 10)
    ret = 0
    ret += f(q, K-1) * r
    ret += f(q-1, K-1) * (9-r)
    ret += f(q, K)
    return ret

print(f(N, K))    


# S = input()
# N = int(S)
# K = int(input())    # K <= 3

# ans = 0
# for i in range(1,N+1):
#     s = str(i)
#     num = 0
#     for c in s:
#         if c != '0':
#             num += 1
#     if len(str(i)) > len(str(i-1)):
#         print(i, ans)
#     if num == K:
#         ans += 1
# print(ans)

# # c = [[0] * (len(S)) for _ in range(3)]
# # for i in range(3):
# #     c[i][0] = 1
# # for i in range(3):
# #     for j in range(1, len(S)):
# #         if i:
# #             c[i][j] = c[i][j-1] + c[i-1][j]
# #         else:
# #             c[i][j] = c[i][j-1] + 1
# # print(c)
# # ans = 0
# # if len(S)-1 >= K:
# #     ans += 9**K * c[K-1][len(S)-2]
# # print(ans)

# # f = [1]
# # for i in range(100):
# #     f.append(f[-1]*(i+1))
# # print(f)

# def f1():
#     res = int(S[0]) + (len(S)-1)*9
#     return res

# def f2():
#     res = (len(S)-2)*9 * (len(S)-3)*9
#     res += int(S[0]) * int(S[1])


# if K == 1:
#     print(f1())
# elif K == 2:
#     print(f2())
