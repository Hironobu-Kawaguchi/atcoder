# https://atcoder.jp/contests/abc131/tasks/abc131_d

N = int(input())

AB = []
for i in range(N):
    a, b = map(int, input().split())
    AB.append([b, a])   # b順にsortするので
AB.sort()

ans = "Yes"
time = 0
for b, a in AB:
    time += a
    if time > b:
        ans = "No"
        break

print(ans)
