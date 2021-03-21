# https://atcoder.jp/contests/arc053/tasks/arc053_b

from collections import Counter
S = input()
n = len(S)
c = Counter(S)
odd = 0
for v in c.values():
    if v%2:
        odd += 1
if odd:
    ans = ((n-odd) // (odd*2)) * 2 + 1
else:
    ans = n
print(ans)
