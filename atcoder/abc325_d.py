# https://atcoder.jp/contests/abc325/tasks/abc325_d

import sys
import heapq

N = int(input())
TD = []
for i in range(N):
    t, d = map(int, input().split())
    TD.append((t, t+d))
TD.sort()

ans = 0
it = 0
now = 0
hq = []
while True:
    if len(hq) == 0:    # nowに印字できる商品がない
        if it == N: break   # 終了
        now = TD[it][0]     # 次の商品が印字機に入る時間へジャンプ
    while it < N and TD[it][0] == now:  # nowに印字機に入る商品をheapqにpush
        heapq.heappush(hq, TD[it][1])
        it += 1
    while len(hq) > 0 and hq[0] < now: heapq.heappop(hq)   # 既に印字機から出た商品をpop
    if len(hq) > 0:     # 印字できる商品があれば印字する
        # print(hq[0], file=sys.stderr)
        heapq.heappop(hq)
        ans += 1
        # break
    now += 1
print(ans)


# N = int(input())
# kugiri_set = set([1])
# TD = []
# for i in range(N):
#     t, d = map(int, input().split())
#     TD.append((t, t+d))
# TD.sort()
# # print(TD)

# ans = 0
# now = 1
# for i, (t, td) in enumerate(TD):
#     if t > now:
#         now = t
#     if t <= now <= td:
#         ans += 1
#         now += 1
# print(ans)
