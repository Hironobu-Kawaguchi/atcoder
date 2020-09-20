# https://atcoder.jp/contests/abc179/tasks/abc179_c

n = int(input())
ans = 0
for a in range(1,n):
    ans += (n-1)//a
print(ans)

# import numpy as np
# n = int(input())
# ans = np.zeros(n, dtype=np.int64)
# for a in range(1,n):
#     ans[a::a] += 1
# print(ans.sum())

