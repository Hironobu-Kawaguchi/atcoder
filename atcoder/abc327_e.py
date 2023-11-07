# https://atcoder.jp/contests/abc327/tasks/abc327_e

import sys

N = int(input())
P = list(map(int, input().split()))

R = [0] * (N + 1)   # R[k]: k個選んだときのレートRの最大値

for i in range(N):
    for k in range(i + 1, 0, -1):
        R[k] = max(R[k], 0.9 * R[k - 1] + P[i])   # DP

div = 1
for k in range(1, N + 1):
    R[k] /= div
    div = div * 0.9 + 1
    R[k] -= 1200 / (k ** 0.5)

print(max(R[1:]))
print(*R[1:], file=sys.stderr)




# import sys
# # input = sys.stdin.buffer.readline
# # def input(): return sys.stdin.readline().rstrip()
# # sys.setrecursionlimit(10 ** 7)

# N = int(input())
# P = list(map(int, input().split()))
# idxP = [(p, N-i-1, i) for i, p in enumerate(P)]
# idxP.sort()
# # idxP.sort(reverse=True)

# pows = [1.0]
# sum_pows = [1.0]
# now = 1.0
# for i in range(N-1):
#     now *= 0.9
#     pows.append(now)
#     sum_pows.append(sum_pows[-1] + now)
# print(*zip(pows, sum_pows), file=sys.stderr)

# def calc(jogai_set):
#     lst = []
#     for i in range(N):
#         if i not in jogai_set:
#             lst.append(P[i])
#     K = len(lst)
#     ret = 0.0
#     for i in range(K):
#         ret += pows[i] * lst[K-i-1]
#     ret /= sum_pows[K-1]
#     ret -= 1200 / (K**0.5)
#     return ret

# # K=Nのとき
# st = set()
# ans = calc(st)
# print(*st, ans, file=sys.stderr)

# # for i in range(N-1, -1, -1):
# for p, _, i in idxP:
#     if len(st) >= N-1: break
#     tmp = calc(st | {i})
#     if tmp > ans:
#         ans = tmp
#         st.add(i)
#         print(*st, ans, file=sys.stderr)
        

# # best = ans
# # while True:
# #     if len(st) >= N-1: break
# #     for i in range(N):
# #         tmp = calc(st | {i})
# #         if tmp > best:
# #             best = tmp
# #             best_i = i
# #     if best > ans:
# #         ans = best
# #         st.add(best_i)
# #     else:
# #         break

# print(ans)
