# https://atcoder.jp/contests/arc001/tasks/arc001_2

from collections import deque
A, B = map(int, input().split())

mv = [+10, +5, +1, -1, -5, -10]
q = deque([(A, 0)])
s = set()
s.add(A)

if A == B:
    goal = True
    print(0)
else:
    goal = False

while goal == False:
    now, n = q.popleft()
    for m in mv:
        nxt = now + m
        if nxt == B:
            print(n+1)
            goal = True
            break
        elif nxt not in s:
            s.add(nxt)
            q.append((nxt, n+1))
