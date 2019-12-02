# https://atcoder.jp/contests/abc003/tasks/abc003_3

N, K = map(int, input().split())
R = list(map(int, input().split()))
R.sort(reverse=True)

ans = 0.0
for i in range(K):
    ans += R[i] / (2**(i+1))

print(ans)
