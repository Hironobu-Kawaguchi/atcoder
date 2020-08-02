# https://atcoder.jp/contests/abc163/tasks/abc163_d

MOD = 10**9+7
N, K = map(int, input().split())
# tmp_mod = pow(10, 100, MOD)

ans = 0
for i in range(K, N+2): # K個以上、N+1以下選ぶ
    minSum = (i-1)*i//2
    maxSum = (2*N+1-i)*i//2
    cnt = maxSum - minSum + 1
    # ans += (minSum + maxSum) * cnt // 2
    # ans += (tmp_mod * cnt * i) % MOD
    ans += cnt
    ans %= MOD

print(ans)

# S = input()
# N = int(input())
# A = list(map(int, (input().split())))
# A = [[int(i) for i in input().split()] for _ in range(N)]
