# https://atcoder.jp/contests/arc036/tasks/arc036_a

N, K = map(int, input().split())
t = [0]
for i in range(N):
    t.append(int(input()))

ans = -1
num = t[0] + t[1] + t[2]
for i in range(3, N+1):
    num += t[i]
    num -= t[i-3]
    if num < K:
        ans = i
        break

print(ans)
