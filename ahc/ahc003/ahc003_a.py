# https://atcoder.jp/contests/ahc003/tasks/ahc003_a

import random
test_num = 10
average = 5000
h = [[average]*29 for _ in range(30)]
v = [[average]*30 for _ in range(29)]

def solve(h, v):
    si, sj, ti, tj = map(int, input().split())
    si -= 1
    sj -= 1
    ti -= 1
    tj -= 1
    s = ''
    if si<ti:
        s += 'D' * (ti-si)
    else:
        s += 'U' * (si-ti)
    if sj<tj:
        s += 'R' * (tj-sj)
    else:
        s += 'L' * (sj-tj)
    
    ans = ['' for _ in range(test_num)]
    test_dist = [0] * test_num
    for k in range(test_num):
        ans[k] = ''.join(random.sample(s, len(s)))
        i, j = si, sj
        for c in ans[k]:
            if c=='D':
                test_dist[k] += v[i][j]
                i += 1
            elif c=='U':
                i -= 1
                test_dist[k] += v[i][j]
            if c=='R':
                test_dist[k] += h[i][j]
                j += 1
            elif c=='L':
                j -= 1
                test_dist[k] += h[i][j]
    best_idx = 0
    best_dist = test_dist[best_idx]
    for k in range(1, test_num):
        if test_dist[k] < best_dist:
            best_idx = k
            best_dist = test_dist[k]

    print(ans[best_idx], flush=True)
    dist = int(input())
    dist_average = dist//len(ans)
    i, j = si, sj
    for c in ans[best_idx]:
        if c=='D':
            v[i][j] = (v[i][j] + dist_average) // 2
            i += 1
        elif c=='U':
            i -= 1
            v[i][j] = (v[i][j] + dist_average) // 2
        if c=='R':
            h[i][j] = (h[i][j] + dist_average) // 2
            j += 1
        elif c=='L':
            j -= 1
            h[i][j] = (h[i][j] + dist_average) // 2
    return

for qi in range(1000):
# for qi in range(2):
    solve(h, v)

# print(h)
# print(v)
