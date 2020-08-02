# https://atcoder.jp/contests/abc064/tasks/abc064_b

N = int(input())
a = list(map(int, input().split()))
a.sort()
ans = a[-1] - a[0]
print(ans)
