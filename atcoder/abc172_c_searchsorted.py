# https://atcoder.jp/contests/abc172/tasks/abc172_c

import numpy as np
import sys
input = sys.stdin.buffer.readline

N, M, K = map(int, input().split())
cumA = np.zeros(N+1, dtype=np.int64)
cumA[1:] = np.array(input().split(), dtype=np.int64).cumsum()
cumB = np.zeros(M+1, dtype=np.int64)
cumB[1:] = np.array(input().split(), dtype=np.int64).cumsum()
# print(cumA)
# print(cumB)

cumA = cumA[cumA <= K]
cumB = cumB[cumB <= K]
ans = np.searchsorted(cumA, K - cumB, side='right') - 1
ans += np.arange(len(cumB))
print(ans.max())

# ans = 0
# for i in range(N, -1, -1):
#     if cumA[i] > K: continue
#     j = np.searchsorted(cumB, K-cumA[i], side='right')
#     ans = max(ans, i+j-1)
# print(ans)

