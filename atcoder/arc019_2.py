# https://atcoder.jp/contests/arc019/tasks/arc019_2

# import numpy as np
import sys
readline = sys.stdin.buffer.readline

# A = np.frombuffer(readline().rstrip(), dtype='S1')
A = readline().rstrip()
# print(A)
L = len(A)
# diff = (A != A[::-1]).sum()
diff = 0
for i in range(L):
    if A[i] != A[L-i-1]:
        diff += 1
# print(diff)

# 回文にする方法がx通りある
if L%2:
    if diff == 0:
        x = 25
    elif diff == 2:
        x = 2
    else:
        x = 0
else:
    if diff == 2:
        x = 2
    else:
        x = 0
ans = L * 25 - x
print(ans)
