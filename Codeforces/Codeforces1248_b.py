# https://codeforces.com/contest/1248/problem/B
# Codeforces Round #594 (Div. 2)

n = int(input())
a = list(map(int, input().split()))
a.sort()
x = sum(a[:n//2])
y = sum(a) - x
ans = x*x + y*y
print(ans)
