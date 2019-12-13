# https://atcoder.jp/contests/agc005/tasks/agc005_a

from collections import deque
X = input()
n = len(X)

q = deque()
for x in X:
    if x == 'S':
        q.append(x)
    else:
        if len(q) == 0 or q[-1] == 'T':
            q.append(x)
        else:
            q.pop()

ans = len(q)
print(ans)
