# https://atcoder.jp/contests/jsc2019-qual/tasks/jsc2019_qual_b

MOD = 1000000007
N, K = map(int, input().split())
A = list(map(int, input().split()))

cnt_in = 0
for i in range(N-1):
    for j in range(i+1, N):
        if A[i] > A[j]:
            cnt_in += 1
ans = (cnt_in * K) % MOD

cnt_next = 0
for i in range(N):
    for j in range(N):
        if A[i] > A[j]:
            cnt_next += 1

ans += (cnt_next * (K*(K-1))//2) % MOD
ans %= MOD

print(int(ans))
