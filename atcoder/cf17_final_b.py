# https://atcoder.jp/contests/cf17-final/tasks/cf17_final_b

from collections import Counter
S = input()
n = len(S)
mx = max(Counter(S).values())
if mx * 3 <= n + 2:
    print('YES')
else:
    print('NO')
