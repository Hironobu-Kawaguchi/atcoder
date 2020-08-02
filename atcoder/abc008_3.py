# https://atcoder.jp/contests/abc008/tasks/abc008_3

N = int(input())
C = [int(input()) for _ in range(N)]

ans = 0.0
for i in range(N):
    cnt = 0
    for j in range(N):
        if i != j and C[i] % C[j] == 0:
            cnt += 1
    if cnt % 2:
        ans += 0.5
    else:
        ans += (cnt+2) / (2*cnt+2)

print(ans)
