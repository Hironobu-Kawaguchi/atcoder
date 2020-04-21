# https://atcoder.jp/contests/arc040/tasks/arc040_c

import numpy as np
N = int(input())
S = np.array([list(input()) for _ in range(N)])
# print(S)

ans = 0
for i in range(N):
    j = np.where(S[i,:]=='.')[0]
    # print(j)
    if j.shape[0] == 0: continue
    S[i,:j[-1]+1] = 'o'
    if i<N-1:
        S[i+1,j[-1]:] = 'o'
    ans += 1

print(ans)
