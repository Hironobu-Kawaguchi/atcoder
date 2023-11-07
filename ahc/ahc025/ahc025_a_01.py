# https://atcoder.jp/contests/ahc025/tasks/ahc025_a

N, D, Q = map(int, input().split())
# W = list(map(int, input().split()))

for qi in range(Q):
    nl, nr = 1, 1
    l = [1]
    r = [2]
    print(nl, nr, *l, *r, flush=True)
    res = input()


d = [-1] * N
for i in range(N):
    d[i] = i % D
print(*d, flush=True)
