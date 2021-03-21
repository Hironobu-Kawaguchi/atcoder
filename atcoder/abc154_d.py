# https://atcoder.jp/contests/abc154/tasks/abc154_d

N, K = map(int, input().split())
p = list(map(int, input().split()))
cum = [sum(p[:K])]
for i in range(N-K):
    cum.append(cum[-1] + p[i+K] - p[i])
ans = (max(cum) + K) / 2
print(ans)
