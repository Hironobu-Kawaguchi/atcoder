# https://atcoder.jp/contests/code-festival-2017-qualb/tasks/code_festival_2017_qualb_b

from collections import Counter
N = int(input())
D = list(map(int, input().split()))
M = int(input())
T = list(map(int, input().split()))

cd = Counter(D)
ct = Counter(T)
ans = 'YES'
for i in ct.keys():
    if cd[i] < ct[i]:
        ans = 'NO'
        break
print(ans)
