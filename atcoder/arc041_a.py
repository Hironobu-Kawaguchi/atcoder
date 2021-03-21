# https://atcoder.jp/contests/arc041/tasks/arc041_a

x, y = map(int, input().split())
k = int(input())

if y >= k:
    ans = x + k
else:
    ans = y + (x-(k-y))
print(ans)
