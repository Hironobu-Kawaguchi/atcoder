# https://atcoder.jp/contests/abc329/tasks/abc329_f

import sys
# input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

N, Q = map(int, (input().split()))
C = list(map(int, (input().split())))

box = [set([C[i]]) for i in range(N)]
for qi in range(Q):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    if len(box[b]) > len(box[a]):
        box[b] |= box[a]
    else:
        box[a] |= box[b]
        box[a], box[b] = box[b], box[a]
    box[a] = set()
    print(len(box[b]))





# N, Q = map(int, (input().split()))
# C = list(map(int, (input().split())))

# box = [set() for _ in range(N)]
# for i in range(N):
#     box[i].add(C[i])

# idx = list(range(N))

# for qi in range(Q):
#     a, b = map(int, input().split())
#     a -= 1; b -= 1
#     if len(box[idx[b]]) >= len(box[idx[a]]):
#         box[idx[b]] |= box[idx[a]]
#         box[idx[a]] = set()
#     else:
#         idx[a], idx[b] = idx[b], idx[a]
#         box[idx[b]] |= box[idx[a]]
#         box[idx[a]] = set()
#     print(len(box[idx[b]]))
#     # print(*idx, file=sys.stderr)
