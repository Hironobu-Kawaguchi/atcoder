# https://atcoder.jp/contests/abc056/tasks/abc056_b

W, a, b = map(int, input().split())
if a > b:
    ans = max(a - (b + W), 0)
else:
    ans = max(b - (a + W), 0)
print(ans)
