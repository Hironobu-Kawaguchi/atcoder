# https://atcoder.jp/contests/abc035/tasks/abc035_b

S = input()
T = int(input())

x, y, q = 0, 0, 0
for c in S:
    if c == 'L':
        x -= 1
    elif c == 'R':
        x += 1
    elif c == 'U':
        y += 1
    elif c == 'D':
        y -= 1
    elif c == '?':
        q += 1

if T == 1:
    ans = abs(x) + abs(y) + q
elif T == 2:
    ans = max(abs(x) + abs(y) - q, len(S) % 2)
print(ans)
