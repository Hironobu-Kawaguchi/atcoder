# https://atcoder.jp/contests/arc014/tasks/arc014_2

N = int(input())
W = [input() for _ in range(N)]
s = set()
ans = "DRAW"
for i in range(N):
    if i:
        if W[i][0] != W[i-1][-1] or W[i] in s:
            if i%2:
                ans = "WIN"
            else:
                ans = "LOSE"
            break
    s.add(W[i])
print(ans)
