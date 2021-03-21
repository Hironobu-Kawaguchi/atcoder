# https://atcoder.jp/contests/agc011/tasks/agc011_a

N, C, K = map(int, input().split())
T = [int(input()) for _ in range(N)]
T.sort()

ans = 1
start = T[0]
cnt = 1
for i in range(1, N):
    cnt += 1
    if T[i] > start + K or cnt > C:
        ans += 1
        cnt = 1
        start = T[i]

print(ans)
