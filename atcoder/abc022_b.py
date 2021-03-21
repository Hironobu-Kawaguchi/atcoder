# https://atcoder.jp/contests/abc022/tasks/abc022_b

N = int(input())
s = set()

ans = 0
for i in range(N):
    A = int(input())
    if A in s:
        ans += 1
    else:
        s.add(A)
print(ans)
