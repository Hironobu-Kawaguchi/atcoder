# D - Crossing
# https://tenka1-2018-beginner.contest.atcoder.jp/tasks/tenka1_2018_d

import itertools
N = int(input())
k = int((2 * N) ** 0.5) + 1
if (k-1) * k == 2 * N:
    print('Yes')
    print(k)
    S = [[] for _ in range(k)]
    n = 1
    for i, j in itertools.combinations(range(k), 2):
        S[i].append(str(n))
        S[j].append(str(n))
        n += 1
    for s in S:
        print(len(s), ' '.join(s))
else:
    print('No')
