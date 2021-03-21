# https://atcoder.jp/contests/abc135/tasks/abc135_a

A, B = map(int, input().split())

if abs(A - B) % 2:
    ans = 'IMPOSSIBLE'
else:
    ans = (A + B) // 2
print(ans)
