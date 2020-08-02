# https://atcoder.jp/contests/abc162/tasks/abc162_e

MOD = 10**9 + 7

N, K = map(int, input().split())

A = [0] * (K + 1)
for d in range(1, K + 1):
    A[d] = pow(K // d, N, MOD)  # 1～Kにdの倍数はK//D個あり、その組み合わせは最大 (K//d)**N ある
# print(A)

for d in range(K, 0, -1):
    for i in range(2, K // d + 1):
        A[d] -= A[d * i]    # dが約数だが最大公約数では無い組み合わせ（dの2～(K//d)倍の組み合わせ）を除外
# print(A)

ans = sum(d * x for d, x in enumerate(A))
ans %= MOD
print(ans)
