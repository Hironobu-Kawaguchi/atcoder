# https://atcoder.jp/contests/agc007/tasks/agc007_a

H, W = map(int, input().split())
A = [input() for _ in range(H)]

ans = "Possible"
now = 0
for i in range(H):
    nxt = now
    for j in range(W):
        if j < now and A[i][j] == '#':
            ans = "Impossible"
        elif j == now:
            if A[i][j] == '.':
                ans = "Impossible"
        else:
            if j == nxt+1 and A[i][j] == '#':
                nxt = j
            elif A[i][j] == '#':
                ans = "Impossible"
    now = nxt

print(ans)
