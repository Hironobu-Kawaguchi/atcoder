# https://atcoder.jp/contests/agc001/tasks/agc001_a

N = int(input())
L = list(map(int, input().split()))
L.sort(reverse=True)

ans = 0
for i in range(N):
    ans += L[2*i+1]
print(ans)
