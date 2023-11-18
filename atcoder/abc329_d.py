# https://atcoder.jp/contests/abc329/tasks/abc329_d

N, M = map(int, (input().split()))
A = list(map(int, (input().split())))

cnt = [0] * N
now = 0
for i in range(M):
    j = A[i] - 1
    cnt[j] += 1
    if cnt[j] > cnt[now] or (cnt[j] >= cnt[now] and j < now):
        now = j
    print(now+1)



# import sys
# # input = sys.stdin.buffer.readline
# # def input(): return sys.stdin.readline().rstrip()
# # sys.setrecursionlimit(10 ** 7)
# import heapq

# N, M = map(int, (input().split()))
# A = list(map(int, (input().split())))

# # idx = [N-i for i in range(N)]
# # cnt = [0] * N           # cnt[j]: 候補者jの現在の得票数
# # for i in range(M):
# #     cnt[A[i]-1] += 1
# #     srt = sorted(zip(cnt, idx), reverse=True)
# #     print(N-srt[0][1]+1)
# #     # print(*srt)

# max = 0
# hq = []
# cnt = [0] * N           # cnt[j]: 候補者jの現在の得票数
# # pos = list(range(N))    # pos[j] = k: 候補者jの現在の順位はk位
# # rank = list(range(N))   # rank[k] = j: 現在の順位k位の候補者はj
# for i in range(M):
#     j = A[i] - 1
#     cnt[j] += 1
#     if cnt[j] > max:
#         max = cnt[j]
#         hq = [j]
#     elif cnt[j] == max:
#         heapq.heappush(hq, j)
#     # k = pos[j]
#     # while k > 0:
#     #     if cnt[rank[k]] > cnt[rank[k-1]] or (cnt[rank[k]] == cnt[rank[k-1]] and rank[k] < rank[k-1]):
#     #         pos[rank[k]], pos[rank[k-1]] = pos[rank[k-1]], pos[rank[k]]
#     #         rank[k], rank[k-1] = rank[k-1], rank[k]
#     #         k -= 1
#     #     else:
#     #         break
#     print(hq[0]+1)
#     # print(*rank)
