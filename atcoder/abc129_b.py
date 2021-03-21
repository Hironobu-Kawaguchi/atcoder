# 
# https://atcoder.jp/contests/abc129/tasks/abc129_a

N = int(input())
W = list(map(int, (input().split())))

Wsum = sum(W)
temp = 0
ans = 10000
for i in range(N):
    temp += W[i]
    ans = min(abs(Wsum - temp * 2), ans)
print(ans)
