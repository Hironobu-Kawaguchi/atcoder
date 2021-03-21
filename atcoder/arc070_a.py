# https://atcoder.jp/contests/abc056/tasks/arc070_a

X = int(input())

ans = 0
sums = 0
while sums < X:
    ans += 1
    sums += ans
print(ans)
