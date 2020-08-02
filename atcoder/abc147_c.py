# https://atcoder.jp/contests/abc147/tasks/abc147_c

N = int(input())
lst = []
for i in range(N):
    A = int(input())
    for j in range(A):
        x, y = map(int, input().split())
        lst.append([i, x-1, y])

ans = 0
for i in range(1 << N):
    chk = []
    for j in range(N):
        if ((i >> j) & 1):
            chk.append(1)
        else:
            chk.append(0)
    for a, x, y in lst:
        if ((i >> a) & chk[a]):
            if chk[x] ^ y:
                chk = [0] * N
                break
    ans = max(ans, sum(chk))

print(ans)
