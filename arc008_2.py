# https://atcoder.jp/contests/arc008/tasks/arc008_2

from collections import Counter
N, M = map(int, input().split())
name = input()
kit = input()

cnt_name = Counter(name)
cnt_kit = Counter(kit)

ans = 0
for k in cnt_name.keys():
    if cnt_kit[k] == 0:
        ans = -1
        break
    else:
        ans = max(ans, (cnt_name[k] + cnt_kit[k] - 1) // cnt_kit[k])
print(ans)
