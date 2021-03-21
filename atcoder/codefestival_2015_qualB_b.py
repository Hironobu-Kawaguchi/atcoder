# https://atcoder.jp/contests/code-festival-2015-qualb/tasks/codefestival_2015_qualB_b
import sys
from collections import Counter
input = sys.stdin.buffer.readline
N, M = map(int, input().split())
A = list(map(int, (input().split())))
cnt = Counter(A)
ans = '?'
for k, v in cnt.items():
    if v*2 > N:
        ans = k
        break
print(ans)
