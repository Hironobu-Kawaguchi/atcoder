# https://atcoder.jp/contests/code-festival-2017-quala/tasks/code_festival_2017_quala_c

from collections import Counter
h, w = map(int, input().split())
a = ''
for i in range(h):
    a += input()
c = Counter(a).values()
m1 ,m2 = 0, 0
for i in c:
    if i%2:
        m1 += 1
    elif i%4 == 2:
        m2 += 1
g1 = h%2 * w%2
g2 = h%2*(w//2) + w%2*(h//2)
# g4 = w//2 * h//2
if m1 <= g1 and m2 <= g2:
    print("Yes")
else:
    print("No")
