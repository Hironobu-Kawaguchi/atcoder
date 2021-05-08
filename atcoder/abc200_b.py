# https://atcoder.jp/contests/abc200/tasks/abc200_b

N, K = map(int, input().split())
for i in range(K):
    if N%200==0:
        N //= 200
    else:
        N *= 1000
        N += 200
print(N)

