# https://atcoder.jp/contests/diverta2019-2/tasks/diverta2019-2_b
import collections
N = int(input())
xy = [[int(i) for i in input().split()] for _ in range(N)]

diff = []

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        else:
            if xy[i][0] > xy[j][0]:
                diff.append((xy[i][0] - xy[j][0], xy[i][1] - xy[j][1]))
            elif xy[i][0] == xy[j][0] and xy[i][1] >= xy[j][1]:
                diff.append((xy[i][0] - xy[j][0], xy[i][1] - xy[j][1]))
            elif xy[i][0] == xy[j][0] and xy[i][1] < xy[j][1]:
                diff.append((xy[j][0] - xy[i][0], xy[j][1] - xy[i][1]))
            else:
                diff.append((xy[j][0] - xy[i][0], xy[j][1] - xy[i][1]))

if N == 1:
    ans = 1
else:
    c = collections.Counter(diff)
    ans = N - sorted(list(c.values()))[-1] // 2
print(ans)
