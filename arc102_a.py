# https://atcoder.jp/contests/abc108/tasks/arc102_a

# TLE

N, K = map(int, input().split())

ans = 0
for a in range(1, N+1):
    cnt = 0
    tmp = K - a % K
    if tmp > N:
        continue
    for b in range(tmp, N+1, K):
        if K - b % K != tmp:
            continue
        for c in range(tmp, N+1, K):
            cnt += 1
    ans += cnt

print(ans)
