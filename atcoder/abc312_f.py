# https://atcoder.jp/contests/abc312/tasks/abc312_f

import sys
input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

N, M = map(int, input().split())
kan0, kan1, kankiri = [], [], []
for _ in range(N):
    t, x = map(int, input().split())
    if t == 0:
        kan0.append(x)
    elif t == 1:
        kan1.append(x)
    else:
        kankiri.append(x)
kan0.sort(reverse=True)
kan1.sort(reverse=True)
kankiri.sort(reverse=True)
# print(kan0, kan1, kankiri, file=sys.stderr)

kan0_idx = min(M, len(kan0))
ans = sum(kan0[:kan0_idx])
kan1_idx = 0
kankiri_cnt = 0
for i in range(min(len(kankiri), M-1)):
    tmp = ans
    if kan0_idx + kan1_idx == M - i:
        if kan1_idx > 0:
            tmp -= kan1[kan1_idx - 1]
            kan1_idx -= 1
            kankiri_cnt += 1
        else:
            tmp -= kan0[kan0_idx - 1]
            kan0_idx -= 1
    kankiri_cnt += kankiri[i]
    while kankiri_cnt > 0 and kan1_idx<len(kan1) and kan0_idx + kan1_idx < M - (i+1):
        tmp += kan1[kan1_idx]
        kankiri_cnt -= 1
        kan1_idx += 1
    # print(tmp, kankiri_cnt, kan0_idx, kan1_idx, file=sys.stderr)
    while kankiri_cnt > 0 and kan0_idx>0 and kan1_idx<len(kan1) and kan0[kan0_idx - 1] < kan1[kan1_idx]:
        tmp += kan1[kan1_idx] - kan0[kan0_idx - 1]
        kankiri_cnt -= 1
        kan0_idx -= 1
        kan1_idx += 1
    # print(tmp, kankiri_cnt, kan0_idx, kan1_idx, file=sys.stderr)
    ans = max(ans, tmp)
print(ans)
