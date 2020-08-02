# B - Foods Loved by Everyone
# https://atcoder.jp/contests/abc118/tasks/abc118_b

N, M = map(int, input().split())

l = [0] * M

for i in range(N):
    a = list(map(int, input().split()))
    for j in range(1, len(a)):
        l[a[j]-1] += 1

print(l.count(N))
